"""Tests for QuantumCircuit simulator."""

import numpy as np

from quantum_simulator import QuantumCircuit


def test_initial_state_is_zero():
    """Fresh circuit should start in |0⟩ state."""
    qc = QuantumCircuit(1)
    probs = qc.probabilities([0])
    assert abs(probs.get("0", 0) - 1.0) < 1e-10


def test_hadamard_creates_superposition():
    """H gate on |0⟩ creates equal superposition."""
    qc = QuantumCircuit(1)
    qc.hadamard(0)
    probs = qc.probabilities([0])
    assert abs(probs.get("0", 0) - 0.5) < 1e-10
    assert abs(probs.get("1", 0) - 0.5) < 1e-10


def test_bell_state_correlation():
    """Bell state |Φ+⟩ should have perfect correlation."""
    qc = QuantumCircuit(2)
    qc.hadamard(0)
    qc.cnot(0, 1)
    probs = qc.probabilities([0, 1])
    # Should only have |00⟩ and |11⟩ with equal probability
    assert abs(probs.get("00", 0) - 0.5) < 1e-10
    assert abs(probs.get("11", 0) - 0.5) < 1e-10
    assert probs.get("01", 0) < 1e-10
    assert probs.get("10", 0) < 1e-10


def test_probabilities_sum_to_one():
    """All measurement probabilities must sum to 1."""
    qc = QuantumCircuit(3)
    qc.hadamard(0)
    qc.hadamard(1)
    qc.cnot(0, 2)
    probs = qc.probabilities([0, 1, 2])
    total = sum(probs.values())
    assert abs(total - 1.0) < 1e-10


def test_x_gate_flips_qubit():
    """X (NOT) gate should flip |0⟩ to |1⟩."""
    qc = QuantumCircuit(1)
    qc.x(0)
    probs = qc.probabilities([0])
    assert abs(probs.get("1", 0) - 1.0) < 1e-10


def test_measurement_collapses_state():
    """After measurement, state should be in a definite classical state."""
    rng = np.random.default_rng(42)
    qc = QuantumCircuit(2)
    qc.hadamard(0)
    qc.cnot(0, 1)
    result = qc.measure(rng=rng)
    # Result must be either {"00": 1} or {"11": 1}
    assert result in ({"00": 1}, {"11": 1})


def test_two_qubit_register():
    """Two-qubit register in |00⟩ should have full probability on "00"."""
    qc = QuantumCircuit(2)
    probs = qc.probabilities([0, 1])
    assert abs(probs.get("00", 0) - 1.0) < 1e-10
