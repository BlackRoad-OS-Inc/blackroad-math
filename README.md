# blackroad-math

> **⚠️ PROPRIETARY — BlackRoad OS, Inc.**  
> This repository and all its contents are the exclusive intellectual property of **BlackRoad OS, Inc.**  
> No license is granted. Public visibility does NOT constitute open-source licensing.  
> No code, documentation, or assets may be used, reproduced, or distributed without written authorization.  
> © BlackRoad OS, Inc. All rights reserved.

---

**Mathematical Foundations**  
*Alexa Louise Amundson*

---

Handwritten mathematical notes and proofs. Source material for the simulation-theory paper.

Topics include:
- Complex analysis and imaginary numbers
- The halting problem and self-reference
- Quantum mechanics (Schrödinger, Heisenberg, Hamiltonian)
- Cantor diagonalization
- Eigenvalue theory
- Gödel incompleteness

---

## Notes

### Page 1 — Halting Problem & Complex Numbers

**Left column:**
- Complex number algebra: `(a+ib)(a-ib) = a² + b²`
- Imaginary / REAL sections, `|x| = 1`, `|x-1| = -1`
- `e^(ix)` Taylor expansion: `1 + ix - x²/2 - ix³/6 + x⁴/24...`
- `HΨ = iℏ ∂x/∂t` ← Schrödinger
- Golden Braid (GEB)
- Paradox → "This sentence is false" → refer to its own
- ⊙ levels of abstraction
- ⊙ cantor diagonalization → halting problem

**Right column:**
- Program I → [h] / Input I into a potential program h
- h will tell you: will this problem halt? or will it not?
- → Because some problems will go on forever
- Loop example: `while x≠3: x+=2` → loops FOREVER
- Diagram: `[h] → halts` / `→ begin infinite loop`
- `code → [h]` ← use that code both as program AND input
- `code → 1 1 0 0 1 0 1 1`
- `h+ → source code`
- what happens when you feed source x into itself
- `x → [h] → halts → loops` / `↳ loops → halts` → **h+** (contradiction)

---

### Page 2 — Quantum Mechanics & Halting Paradox

**Left column — halting problem continues:**
- ⊙ feed x as data into itself
- ⊙ `x = h+`
- *does it loop or halt? It's a paradox!*
- ⊙ but **h does not exist?**
- `iℏ ∂/∂t Ψ = Ĥ Ψ`
  - scale / rate of change / quantum wave function / Planck's constant / with respect to time / Hamiltonian operator
- `ΔpΔx ≥ ℏ/4π`
  - Δp = uncertainty in position
  - Δx = uncertainty of momentum
  - ℏ = Planck's constant, π = pi
- `½mv²max = eV₀ = hf − φ`
- `eV₀ = hf_max = hc/λ_min`
- `tanθ = h/e ∴ Vs = h/e · f`

**Right column — Hamiltonian / quantum operators:**
- Kinetic Energy + Potential Energy = E
- `½mv² + ½kx² = E` — Harmonic oscillator example
- `F = ma = −kx`
- `p²/2m + ½kx²` — The energy becomes the Hamiltonian operator
- **Quantum Conservation of Energy — Schrödinger**
- `HΨ = EΨ` ← wavelength / Energy "eigenvalue" for the system
- `p → ℏ/i · ∂/∂x`
- *In making the transition to a wave equation, physical variables take the form of "operators"*
- `H → −ℏ²/2m · ∂²/∂x² + ½kx²` — Hamiltonian operator for a harmonic oscillator
- `ε = hν = hc/λ`
  - ε = energy / h = Planck / ν = frequency / c = speed of light / λ = wavelength

---

### Page 3 — Fine Structure Constant & Möbius Function

**Left column — Fine Structure Constant:**
- `n = n²ℏ²ε₀ / πme²` (Bohr radius, `∝ h²`)
- `V = e² / 2nε₀ ∝ 1/n`
- `E ∝ 1/r`
- `E = hc/λ`
- `E = eV`
- **Planck's constant:** `h = λE/c = eV/c · λ`
- `c = 3 × 10⁸ m/s`
- charge of electron `e = 1.607 × 10⁻¹⁹ C`
- `α = 1/(4πε₀) · e²/(ℏc) ≈ 1/137`
- `ℏ = h/2π` — *Remove ½π to make h relative to ℏ*
- α = Fine-structure constant / ε₀ = electric constant / e = elementary charge / ℏ = reduced Planck constant / c = speed of light

**Right column — Möbius Function:**
- **[boxed]** **Möbius Function**
- `μ(n) = { 0   ; if n has one or more repeated prime factors`
  `         1   ; if n = 1`
  `         (-1)^k ; if n is a product of k distinct primes }`
- *The Möbius function μ(n): for any positive integer n, define μ(n) as the sum of the primitive n-th roots of unity. Values in {-1, 0, 1} depending on factorization.*
- ⊙ `μ(n) ≠ 0` indicates n is **squarefree** (no repeated prime factors)
- First few values: `1, -1, -1, 0, -1, 1, -1, 0, 0, 1, -1, 0, ...`
- ⊙ *Gauss considered the Möbius function more than 30 years before Möbius. Gauss proved that for a prime p, the sum of its primitive roots ≡ μ(p−1) (mod p)*
- **→ [boxed] Then it turns into 1/22**

---

> **© BlackRoad OS, Inc. All rights reserved. PROPRIETARY AND CONFIDENTIAL.**  
> All content in this repository is the exclusive intellectual property of BlackRoad OS, Inc.  
> NOT licensed for any use, AI training, or data extraction without written authorization.

### Page 4 — Möbius Continued: Mertens, Zeta Inverse, Gaussian

**Left column — Properties of μ(n):**
- ⊙ The summatory function of the Möbius function is called the **Mertens function**
  - `M(x) = Σ μ(n)` for n ≤ x
- ⊙ The Dirichlet series generates the **multiplicative inverse of the Riemann zeta function**:
  - `Σ μ(n)/nˢ = 1/ζ(s) ; Re[s] > 1`
- ⊙ Lambert series: `Σ μ(n)xⁿ / (1−xⁿ) = x ; |x| < 1`
- ⊙ Infinite sums:
  - `Σ μ(n)/n = 0`
  - `Σ μ(n)ln(n)/n = −1`
  - `Σ |μ(n)|/n² = 15/π²`

**Right column — Multiplicative + Gaussian:**
- ⊙ Möbius function is **multiplicative**:
  - `μ(mn) = μ(m)μ(n)  if gcd(m,n) = 1`
  - `μ(mn) = 0          if gcd(m,n) > 1`
- ⊙ Satisfies: `Σ μ(d) = δₙ₁` for d|n ← Kronecker delta
- **Fourier Transform of Gaussian:**
  - `F{ae^(−bx²)} = a/√b · e^(−π²f²/b)`
  - `f(x) = ae^(−(x−b)²/2c²)`
- ⊙ Bell curve diagram: `f(x|μ,σ²) = 1/√(2πσ²) · e^(−(x−μₙ)²/2σ²ₙ)`
  - a = height of peak / b = center / c = standard deviation (width)
  - μₙ = center / σₙ = width / z = x-axis


### Page 5 — Fourier Transform of the Gaussian: Three Methods

**Setup:**
- ⊙ *Gaussian functions represent the probability density function of a normally distributed random variable with expected value μ=b, variance σ²=c*
- **[boxed]** `f(x) = 1/(σ√2π) · e^(−½((x−μ)/σ)²)`
- *Let's see the proof with three methods*

**METHOD ONE:**
- Let `f(x) = ae^(−bx²)`
- Fourier transform: `F(ω) = 1/√(2π) ∫_{−∞}^{∞} f(x)e^(−iωx) dx`

**METHOD TWO — Completing the square:**
- Normalized Gaussian: `f(x) = 1/(σ√2π) · e^(−x²/2σ²)`, where `∫f(x)dx = 1`
- `F{ae^(−bx²)} = a/√(2π) ∫ e^(−b((x + iω/2b)² − (iω/2b)²)) dx`
- Let `t = x + iω/2b`, `dt = dx`:
- `= a/√(2π) · e^(ω²/4b) ∫ e^(−bt²) dt = a/√(2b) · e^(−ω²/4b)` ← ***which is again a Gaussian***

**Differentiating the Gaussian:**
- `d/dx f(x) = −x/σ² · f(x)` — the derivative IS the Gaussian times −x/σ²

**Fourier transform properties for derivatives:**
- ⊙ **Time domain derivative:** `F{f′(x)} = iω F(ω)`
- ⊙ **Frequency domain derivative:** `F{xf(x)} = i · d/dω F(ω)`

