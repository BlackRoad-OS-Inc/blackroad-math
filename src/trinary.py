"""
BlackRoad Math — Trinary Logic System
Values: 1=True, 0=Unknown, -1=False
"""

from __future__ import annotations

from typing import Union

TruthValue = Union[int, float]


class Trinary:
    """Trinary logic value with paraconsistent operations."""

    TRUE = 1
    UNKNOWN = 0
    FALSE = -1

    def __init__(self, value: TruthValue):
        self.v = max(-1, min(1, value))

    def __repr__(self):
        if self.v == 1:
            return "TRUE"
        if self.v == -1:
            return "FALSE"
        return f"UNKNOWN({self.v:.2f})"

    def __and__(self, other: Trinary) -> Trinary:
        # Kleene strong AND
        return Trinary(min(self.v, other.v))

    def __or__(self, other: Trinary) -> Trinary:
        # Kleene strong OR
        return Trinary(max(self.v, other.v))

    def __invert__(self) -> Trinary:
        return Trinary(-self.v)

    def implies(self, other: Trinary) -> Trinary:
        # A → B = ¬A ∨ B
        return (~self) | other

    def confidence(self) -> float:
        """Distance from unknown (0 = fully unknown, 1 = fully certain)."""
        return abs(self.v)

    @classmethod
    def from_probability(cls, p: float) -> Trinary:
        """Map [0,1] probability to [-1,1] trinary space."""
        return cls(2 * p - 1)

    @classmethod
    def aggregate(cls, values: list[Trinary], weights: list[float] = None) -> Trinary:
        """Aggregate multiple trinary values (majority with optional weighting)."""
        if not values:
            return cls(0)
        w = weights or [1.0] * len(values)
        total_weight = sum(w)
        weighted_sum = sum(v.v * wi for v, wi in zip(values, w))
        return cls(weighted_sum / total_weight)


class BeliefState:
    """Track belief states for multiple claims using trinary logic."""

    def __init__(self):
        self._beliefs: dict[str, Trinary] = {}
        self._quarantined: set[str] = set()

    def assert_true(self, claim: str, confidence: float = 1.0):
        self._beliefs[claim] = Trinary(confidence)

    def assert_false(self, claim: str, confidence: float = 1.0):
        self._beliefs[claim] = Trinary(-confidence)

    def observe(self, claim: str, value: float = 0.0):
        self._beliefs[claim] = Trinary(value)

    def quarantine(self, claim: str):
        """Mark claim as contradictory — remove from reasoning."""
        self._quarantined.add(claim)
        self._beliefs[claim] = Trinary(0)

    def evaluate(self, claim: str) -> Trinary:
        if claim in self._quarantined:
            return Trinary(0)
        return self._beliefs.get(claim, Trinary(0))

    def detect_contradictions(self) -> list[tuple[str, str]]:
        contradictions = []
        claims = list(self._beliefs.keys())
        for i, c1 in enumerate(claims):
            neg_c1 = f"not_{c1}"
            if neg_c1 in self._beliefs:
                v1 = self._beliefs[c1]
                v2 = self._beliefs[neg_c1]
                if v1.v > 0 and v2.v > 0:
                    contradictions.append((c1, neg_c1))
        return contradictions


if __name__ == "__main__":
    a = Trinary(1)  # TRUE
    b = Trinary(-1)  # FALSE
    u = Trinary(0)  # UNKNOWN

    print(f"TRUE AND FALSE = {a & b}")  # FALSE
    print(f"TRUE OR FALSE  = {a | b}")  # TRUE
    print(f"NOT UNKNOWN    = {~u}")  # UNKNOWN
    print(f"TRUE implies UNKNOWN = {a.implies(u)}")  # UNKNOWN

    belief = BeliefState()
    belief.assert_true("gateway_is_tokenless", confidence=1.0)
    belief.assert_true("agents_run_locally", confidence=0.9)
    belief.observe("network_latency_high", value=0.3)

    print(f"\nGateway tokenless: {belief.evaluate('gateway_is_tokenless')}")
    print(f"Agents local: {belief.evaluate('agents_run_locally')}")
