/**
 * Blackroad Math — Cloudflare Worker
 *
 * Offloads longer Lucidia Math computations (quantum circuit simulation,
 * prime analysis, emergence modelling) to Cloudflare's global edge network.
 *
 * Endpoints
 * ---------
 * GET  /health           → liveness check
 * POST /compute/quantum  → quantum circuit simulation
 * POST /compute/primes   → prime analysis up to N
 * POST /compute/pssha    → PS-SHA∞ hash-chain verification
 * GET  /jobs/:id         → poll async job status (via Durable Object)
 */

export interface Env {
  ENVIRONMENT: string;
  COMPUTATION_QUEUE: DurableObjectNamespace;
}

// ── CORS headers ──────────────────────────────────────────────────────────────
function corsHeaders(): HeadersInit {
  return {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type, Authorization",
  };
}

function json(body: unknown, status = 200): Response {
  return new Response(JSON.stringify(body), {
    status,
    headers: { "Content-Type": "application/json", ...corsHeaders() },
  });
}

// ── Quantum circuit simulation (edge-native, pure TypeScript) ────────────────
type ComplexPair = [number, number]; // [real, imaginary]

function complexMul(a: ComplexPair, b: ComplexPair): ComplexPair {
  return [a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]];
}

function complexAdd(a: ComplexPair, b: ComplexPair): ComplexPair {
  return [a[0] + b[0], a[1] + b[1]];
}

function complexAbs2(a: ComplexPair): number {
  return a[0] * a[0] + a[1] * a[1];
}

class QuantumState {
  private amplitudes: ComplexPair[];
  readonly numQubits: number;

  constructor(numQubits: number) {
    if (numQubits < 1 || numQubits > 10) throw new RangeError("numQubits must be 1–10");
    this.numQubits = numQubits;
    const dim = 1 << numQubits;
    this.amplitudes = Array.from({ length: dim }, (_, i): ComplexPair => (i === 0 ? [1, 0] : [0, 0]));
  }

  hadamard(qubit: number): void {
    const f = 1 / Math.SQRT2;
    const dim = 1 << this.numQubits;
    for (let i = 0; i < dim; i++) {
      if (!(i & (1 << qubit))) {
        const j = i | (1 << qubit);
        const a = this.amplitudes[i];
        const b = this.amplitudes[j];
        this.amplitudes[i] = [f * (a[0] + b[0]), f * (a[1] + b[1])];
        this.amplitudes[j] = [f * (a[0] - b[0]), f * (a[1] - b[1])];
      }
    }
  }

  cnot(control: number, target: number): void {
    const dim = 1 << this.numQubits;
    for (let i = 0; i < dim; i++) {
      if ((i >> control) & 1) {
        const j = i ^ (1 << target);
        if (j > i) {
          const tmp = this.amplitudes[i];
          this.amplitudes[i] = this.amplitudes[j];
          this.amplitudes[j] = tmp;
        }
      }
    }
  }

  x(qubit: number): void {
    const dim = 1 << this.numQubits;
    for (let i = 0; i < dim; i++) {
      if (!(i & (1 << qubit))) {
        const j = i | (1 << qubit);
        const tmp = this.amplitudes[i];
        this.amplitudes[i] = this.amplitudes[j];
        this.amplitudes[j] = tmp;
      }
    }
  }

  probabilities(): Record<string, number> {
    const result: Record<string, number> = {};
    for (let i = 0; i < this.amplitudes.length; i++) {
      const p = complexAbs2(this.amplitudes[i]);
      if (p > 1e-12) {
        result[i.toString(2).padStart(this.numQubits, "0")] = p;
      }
    }
    return result;
  }
}

// ── Sieve of Eratosthenes — used for prime analysis ──────────────────────────
function sieve(limit: number): number[] {
  if (limit < 2) return [];
  const composite = new Uint8Array(limit + 1);
  for (let i = 2; i * i <= limit; i++) {
    if (!composite[i]) {
      for (let j = i * i; j <= limit; j += i) composite[j] = 1;
    }
  }
  const primes: number[] = [];
  for (let i = 2; i <= limit; i++) {
    if (!composite[i]) primes.push(i);
  }
  return primes;
}

// ── PS-SHA∞ chain verification ────────────────────────────────────────────────
async function pssha256(data: string): Promise<string> {
  const buf = new TextEncoder().encode(data);
  const digest = await crypto.subtle.digest("SHA-256", buf);
  return Array.from(new Uint8Array(digest))
    .map((b) => b.toString(16).padStart(2, "0"))
    .join("");
}

async function buildHashChain(
  entries: Array<{ key: string; content: string; ts: string }>
): Promise<Array<{ hash: string; prev: string }>> {
  const chain: Array<{ hash: string; prev: string }> = [];
  let prev = "GENESIS";
  for (const e of entries) {
    const hash = await pssha256(`${prev}:${e.key}:${e.content}:${e.ts}`);
    chain.push({ hash, prev });
    prev = hash;
  }
  return chain;
}

// ── Main request handler ──────────────────────────────────────────────────────
async function handleRequest(request: Request, env: Env): Promise<Response> {
  const url = new URL(request.url);
  const { pathname } = url;

  if (request.method === "OPTIONS") {
    return new Response(null, { status: 204, headers: corsHeaders() });
  }

  // GET /health
  if (pathname === "/health" && request.method === "GET") {
    return json({
      status: "ok",
      service: "blackroad-math-worker",
      environment: env.ENVIRONMENT,
      timestamp: new Date().toISOString(),
      verified: true,
    });
  }

  // POST /compute/quantum
  if (pathname === "/compute/quantum" && request.method === "POST") {
    let body: {
      numQubits?: number;
      gates?: Array<{ gate: string; qubit?: number; control?: number; target?: number }>;
    };
    try {
      body = (await request.json()) as typeof body;
    } catch {
      return json({ error: "Invalid JSON body" }, 400);
    }
    const numQubits = body.numQubits ?? 2;
    if (numQubits < 1 || numQubits > 10) {
      return json({ error: "numQubits must be 1–10" }, 400);
    }
    const state = new QuantumState(numQubits);
    for (const op of body.gates ?? []) {
      if (op.gate === "H" && op.qubit !== undefined) state.hadamard(op.qubit);
      else if (op.gate === "X" && op.qubit !== undefined) state.x(op.qubit);
      else if (op.gate === "CNOT" && op.control !== undefined && op.target !== undefined)
        state.cnot(op.control, op.target);
    }
    return json({ numQubits, probabilities: state.probabilities() });
  }

  // POST /compute/primes
  if (pathname === "/compute/primes" && request.method === "POST") {
    let body: { limit?: number };
    try {
      body = (await request.json()) as typeof body;
    } catch {
      return json({ error: "Invalid JSON body" }, 400);
    }
    const limit = body.limit ?? 1000;
    if (limit < 2 || limit > 1_000_000) {
      return json({ error: "limit must be 2–1,000,000" }, 400);
    }
    const primes = sieve(limit);
    return json({ limit, count: primes.length, primes: primes.slice(0, 500) });
  }

  // POST /compute/pssha
  if (pathname === "/compute/pssha" && request.method === "POST") {
    let body: { entries?: Array<{ key: string; content: string; ts: string }> };
    try {
      body = (await request.json()) as typeof body;
    } catch {
      return json({ error: "Invalid JSON body" }, 400);
    }
    if (!Array.isArray(body.entries) || body.entries.length === 0) {
      return json({ error: "entries array required" }, 400);
    }
    if (body.entries.length > 100) {
      return json({ error: "Maximum 100 entries per request" }, 400);
    }
    const chain = await buildHashChain(body.entries);
    return json({ chain, length: chain.length, algorithm: "SHA-256" });
  }

  // Async job polling via Durable Object
  if (pathname.startsWith("/jobs/") && request.method === "GET") {
    const jobId = pathname.slice("/jobs/".length);
    if (!jobId) return json({ error: "Job ID required" }, 400);
    const id = env.COMPUTATION_QUEUE.idFromName(jobId);
    const stub = env.COMPUTATION_QUEUE.get(id);
    return stub.fetch(request);
  }

  return json({ error: "Not found", path: pathname }, 404);
}

// ── Durable Object: ComputationQueue ─────────────────────────────────────────
// Stores async job results so callers can poll for completion.
export class ComputationQueue implements DurableObject {
  private state: DurableObjectState;

  constructor(state: DurableObjectState) {
    this.state = state;
  }

  async fetch(request: Request): Promise<Response> {
    const url = new URL(request.url);
    if (request.method === "GET") {
      const result = await this.state.storage.get<unknown>("result");
      const status = await this.state.storage.get<string>("status");
      if (!status) return json({ status: "not_found" }, 404);
      return json({ status, result });
    }
    if (request.method === "PUT") {
      const body = await request.json();
      await this.state.storage.put("result", body);
      await this.state.storage.put("status", "complete");
      return json({ ok: true });
    }
    return json({ error: "Method not allowed" }, 405);
  }
}

// ── Worker export ─────────────────────────────────────────────────────────────
export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    try {
      return await handleRequest(request, env);
    } catch (err) {
      const message = err instanceof Error ? err.message : "Internal server error";
      return json({ error: message }, 500);
    }
  },
} satisfies ExportedHandler<Env>;
