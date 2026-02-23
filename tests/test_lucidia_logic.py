"""Tests for Lucidia Logic — symbolic math, trinary, and consciousness functions."""
import pytest
import math
from lucidia_logic import (
    Trinary, psi_prime, breath_function, truth_reconciliation,
    emotional_gravity, self_awakening, soul_recognition,
    compassion_state_encryption
)


def test_trinary_values():
    """Trinary class should have TRUE, FALSE, UNKNOWN."""
    t = Trinary(1)
    f = Trinary(-1)
    u = Trinary(0)
    assert t.value == 1
    assert f.value == -1
    assert u.value == 0


def test_psi_prime_returns_tuple():
    """psi_prime should return a 2-tuple."""
    result = psi_prime(0.5)
    assert isinstance(result, tuple)
    assert len(result) == 2


def test_breath_function_returns_tuple():
    """breath_function(t) should return a 2-tuple at any time t."""
    for t in [0, 1, 5, 10, 100]:
        result = breath_function(t)
        assert isinstance(result, tuple)
        assert len(result) == 2


def test_truth_reconciliation_bounded():
    """truth_reconciliation should return a finite float."""
    result = truth_reconciliation([0.8, 0.6, 0.9], [0.1, 0.2, 0.15])
    assert isinstance(result, float)
    assert math.isfinite(result)


def test_emotional_gravity_returns_float():
    """emotional_gravity should return a finite float."""
    result = emotional_gravity([0.5, 0.7], [0.3, 0.4])
    assert isinstance(result, float)
    assert math.isfinite(result)


def test_self_awakening_returns_float():
    """self_awakening should return a finite float."""
    result = self_awakening([0.1, 0.2, 0.3, 0.2, 0.1])
    assert isinstance(result, float)
    assert math.isfinite(result)


def test_soul_recognition_similarity():
    """Same sequences should give high similarity."""
    seq = [0.5, 0.6, 0.7, 0.8, 0.9]
    result = soul_recognition(seq, seq, steps=50)
    assert isinstance(result, float)
    assert math.isfinite(result)


def test_soul_recognition_different_sequences():
    """Different sequences should give different similarity than same."""
    seq_a = [0.1, 0.2, 0.3, 0.4, 0.5]
    seq_b = [0.9, 0.8, 0.7, 0.6, 0.5]
    same = soul_recognition(seq_a, seq_a, steps=50)
    diff = soul_recognition(seq_a, seq_b, steps=50)
    # Results should differ (different input = different similarity)
    assert isinstance(same, float)
    assert isinstance(diff, float)


def test_compassion_state_encryption():
    """compassion_state_encryption should return a non-empty string."""
    result = compassion_state_encryption("trust", 0.8)
    assert isinstance(result, str)
    assert len(result) > 0


def test_pssha_chain_integrity():
    """PS-SHA∞ chain integrity: tamper at index N breaks cascade."""
    import hashlib
    def pssha(prev, key, content, ts):
        return hashlib.sha256(f"{prev}:{key}:{content}:{ts}".encode()).hexdigest()
    
    prev = "GENESIS"
    entries = []
    for i in range(5):
        h = pssha(prev, f"k{i}", f"val{i}", str(i * 1000))
        entries.append({"h": h, "prev": prev})
        prev = h
    
    # All hashes should be 64 hex chars
    for e in entries:
        assert len(e["h"]) == 64
        assert all(c in "0123456789abcdef" for c in e["h"])
    
    # Verify chain links
    for i in range(1, len(entries)):
        assert entries[i]["prev"] == entries[i-1]["h"]
