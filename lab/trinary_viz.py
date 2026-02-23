#!/usr/bin/env python3
"""
Trinary Logic ASCII Visualizer — Łukasiewicz Three-Valued Logic
Truth states: 1 (True), 0 (Unknown), -1 (False)
"""

from itertools import product

STATES = {1: "T", 0: "U", -1: "F"}
COLORS = {1: "\033[32m", 0: "\033[33m", -1: "\033[31m"}
RESET = "\033[0m"


def neg(a: int) -> int:
    """Łukasiewicz negation: ¬a = -a"""
    return -a


def conj(a: int, b: int) -> int:
    """Łukasiewicz conjunction: a ∧ b = min(a, b)"""
    return min(a, b)


def disj(a: int, b: int) -> int:
    """Łukasiewicz disjunction: a ∨ b = max(a, b)"""
    return max(a, b)


def impl(a: int, b: int) -> int:
    """Łukasiewicz implication: a → b"""
    return min(1, 1 - a + b)


def equiv(a: int, b: int) -> int:
    """Łukasiewicz equivalence: a ↔ b = (a → b) ∧ (b → a)"""
    return conj(impl(a, b), impl(b, a))


def _col(v: int) -> str:
    return f"{COLORS[v]}{STATES[v]}{RESET}"


def print_unary_table(op_name: str, op):
    print(f"\n{'─'*30}")
    print(f"  ¬ (negation)   op={op_name}")
    print(f"  {'A':^5} │ {'¬A':^5}")
    print(f"  {'─'*5}─┼─{'─'*5}")
    for a in [1, 0, -1]:
        print(f"  {_col(a):^14} │ {_col(op(a)):^14}")


def print_binary_table(op_name: str, symbol: str, op):
    print(f"\n{'─'*40}")
    print(f"  {symbol} ({op_name})")
    header = f"  {'A':^5} {'B':^5} │ {'Result':^8}"
    print(header)
    print(f"  {'─'*11}─┼─{'─'*8}")
    for a, b in product([1, 0, -1], repeat=2):
        r = op(a, b)
        print(f"  {_col(a):^14} {_col(b):^14} │ {_col(r):^17}")


def print_ps_sha_truth_states():
    """PS-SHA∞ memory truth state semantics."""
    print(f"\n{'═'*50}")
    print("  PS-SHA∞ Memory Chain — Truth State Semantics")
    print(f"{'═'*50}")
    rows = [
        (1, "True", "Verified fact — fully committed"),
        (0, "Unknown", "Observation — under evaluation"),
        (-1, "False", "Disproven — quarantined in chain"),
    ]
    for ts, label, desc in rows:
        print(f"  {_col(ts)} ({ts:+d})  {label:<10}  {desc}")
    print()


def contradiction_check(a: int, b: int) -> str:
    """Detect if two truth states form a contradiction."""
    e = equiv(a, b)
    if e == -1:
        return "CONTRADICTION — quarantine both claims"
    elif e == 0:
        return "UNCERTAIN — gather more evidence"
    else:
        return "CONSISTENT"


def interactive_mode():
    print("\n  Interactive Mode — enter two truth states (1/0/-1) to check consistency")
    while True:
        try:
            raw = input("  a b (or q to quit): ").strip()
            if raw.lower() in ("q", "quit", "exit"):
                break
            parts = raw.split()
            a, b = int(parts[0]), int(parts[1])
            if a not in (1, 0, -1) or b not in (1, 0, -1):
                raise ValueError
            result = contradiction_check(a, b)
            print(f"  {_col(a)} {_col(b)}  →  {result}")
        except (ValueError, IndexError):
            print("  Invalid input. Use: 1 0 / 0 -1 / 1 1 etc.")
        except (EOFError, KeyboardInterrupt):
            break


def main():
    print("\n╔══════════════════════════════════════════════════════╗")
    print("║   BlackRoad Trinary Logic Visualizer                 ║")
    print("║   Łukasiewicz Three-Valued Logic (T / U / F)         ║")
    print("╚══════════════════════════════════════════════════════╝")

    print_unary_table("Łukasiewicz Negation", neg)
    print_binary_table("conjunction", "∧", conj)
    print_binary_table("disjunction", "∨", disj)
    print_binary_table("implication", "→", impl)
    print_binary_table("equivalence", "↔", equiv)
    print_ps_sha_truth_states()

    # Demonstrate contradiction detection
    print(f"\n{'─'*50}")
    print("  Contradiction Detection Demo")
    print(f"{'─'*50}")
    pairs = [(1, -1), (1, 0), (0, 0), (-1, -1)]
    for a, b in pairs:
        print(f"  {_col(a)} vs {_col(b)}: {contradiction_check(a, b)}")

    import sys
    if "--interactive" in sys.argv or "-i" in sys.argv:
        interactive_mode()


if __name__ == "__main__":
    main()
