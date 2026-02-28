# BlackRoad Math - Copilot Instructions

## Project Overview

BlackRoad Math is the mathematical foundation library for BlackRoad OS. It implements trinary logic, quantum simulation, consciousness modeling, and advanced mathematical engines for the BlackRoad ecosystem.

**Key components:**
- **forge/**: Mathematical engines — consciousness modeling, unified geometry, fractals, operators, proofs
- **lab/**: Experimental math — Amundson equations, quantum finance, prime exploration, trinary extensions
- **agents/**: AI agent modules — codex, emotional, guardian, memory, spiral, video agents
- **src/**: Core trinary logic implementation
- **quantum_simulator.py**: State-vector quantum circuit simulator
- **lucidia_logic.py**: Symbolic/mathematical functions for the Lucidia project

## Architecture

### Module Structure
```
blackroad-math/
├── forge/              # Production math engines
│   ├── consciousness.py
│   ├── unified_geometry.py
│   ├── fractals.py
│   ├── operators.py
│   └── proofs.py
├── lab/                # Experimental / research
│   ├── amundson_equations.py
│   ├── quantum_finance.py
│   ├── prime_explorer.py
│   └── trinary_logic.py
├── agents/             # Agent modules
├── src/                # Core implementations
│   └── trinary.py
├── tests/              # Test suite
└── quantum_simulator.py
```

## Build & Test Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Run all tests
pytest tests/ -v --tb=short

# Run with coverage
pytest tests/ --cov=. --cov-report=term-missing -q

# Type checking
mypy quantum_simulator.py lucidia_logic.py --ignore-missing-imports

# Linting
ruff check .
black --check .
```

## Key Conventions

### Python Style
- Follow PEP 8
- Use type hints
- Line length: 100 characters (configured in pyproject.toml)
- Use `black` for formatting, `ruff` for linting
- Document with docstrings (NumPy style for public APIs)

### Trinary Logic
The core trinary system uses values `{-1, 0, +1}`:
- `+1` = True
- `0` = Unknown
- `-1` = False

### Mathematical Functions
- Pure Python where possible for transparency
- NumPy for quantum simulation and numerical work
- SymPy for symbolic computation
- All math functions should include docstrings with formulas

### Testing Guidelines
- Tests live in `tests/`
- Use `pytest` for all testing
- Test mathematical edge cases (zero, negative, boundary values)
- Include property-based tests where appropriate

## Security Considerations

- No secrets in code (use .env for configuration)
- Mathematical functions should validate inputs
- Quantum simulator should handle degenerate states gracefully

## Project Philosophy

1. **Mathematical rigor**: Implementations should be correct and well-documented
2. **Trinary-first**: The trinary logic system `{-1, 0, +1}` is foundational
3. **Transparency**: Pure Python for readability, NumPy only where needed
4. **Testability**: Every mathematical function should be testable
5. **Proprietary**: All code is © BlackRoad OS, Inc. — not open source
