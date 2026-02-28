# Contributing to BlackRoad Math

> Thank you for your interest in contributing to BlackRoad Math!

---

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Making Changes](#making-changes)
- [Pull Request Process](#pull-request-process)
- [Coding Standards](#coding-standards)
- [Testing Guidelines](#testing-guidelines)
- [Documentation](#documentation)
- [Community](#community)

---

## Code of Conduct

### Our Pledge

We pledge to make participation in our project a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, gender identity, level of experience, nationality, personal appearance, race, religion, or sexual identity and orientation.

### Our Standards

**Positive behaviors:**
- Using welcoming and inclusive language
- Being respectful of differing viewpoints
- Gracefully accepting constructive criticism
- Focusing on what is best for the community

**Unacceptable behaviors:**
- Trolling, insulting comments, personal attacks
- Public or private harassment
- Publishing others' private information
- Other conduct which could be considered inappropriate

---

## Getting Started

### Types of Contributions

| Type | Description | Difficulty |
|------|-------------|------------|
| 🐛 Bug fixes | Fix reported issues | Easy-Medium |
| 📝 Documentation | Improve docs, fix typos | Easy |
| ✨ Features | Add new functionality | Medium-Hard |
| 🧪 Tests | Add test coverage | Medium |
| 🔧 Tooling | Improve dev experience | Medium |
| 🎨 Design | UI/UX improvements | Medium |

### Good First Issues

Look for issues labeled:
- `good first issue` - Great for newcomers
- `help wanted` - We need help!
- `documentation` - Doc improvements
- `bug` - Confirmed bugs

---

## Development Setup

### Prerequisites

```bash
# Required
python >= 3.10

# Recommended
pip >= 23.0
```

### Clone & Install

```bash
# Clone the repository
git clone https://github.com/BlackRoad-OS-Inc/blackroad-math.git
cd blackroad-math

# Install dependencies
pip install -r requirements.txt

# Set up environment
cp .env.example .env

# Verify setup
pytest tests/ -v
```

### Project Structure

```
blackroad-math/
├── forge/              # Production math engines
├── lab/                # Experimental / research
├── agents/             # Agent modules
├── src/                # Core implementations
├── tests/              # Test suite
├── quantum_simulator.py
└── lucidia_logic.py
```

---

## Making Changes

### Branch Naming

```
feature/short-description    # New features
fix/issue-number-description # Bug fixes
docs/what-changed           # Documentation
refactor/what-changed       # Code refactoring
test/what-testing           # Test additions
```

### Commit Messages

Follow [Conventional Commits](https://conventionalcommits.org/):

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `style`: Formatting
- `refactor`: Code restructuring
- `test`: Adding tests
- `chore`: Maintenance

**Examples:**
```
feat(trinary): add weighted aggregation for belief states

fix(quantum): resolve normalization edge case in measurement
Closes #123

docs(readme): update installation instructions
```

### Code Changes Workflow

```
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Write/update tests
5. Update documentation
6. Run linting & tests
7. Commit with good messages
8. Push to your fork
9. Open a Pull Request
```

---

## Pull Request Process

### Before Submitting

- [ ] Code follows style guidelines
- [ ] Tests pass locally
- [ ] Documentation updated
- [ ] Commit messages follow convention
- [ ] Branch is up to date with main

### Review Process

1. **Automated checks** run (lint, test, build)
2. **Code review** by maintainer
3. **Changes requested** or **approved**
4. **Merged** to main branch

### Review Timeline

| PR Size | Expected Review Time |
|---------|---------------------|
| Small (<100 lines) | 1-2 days |
| Medium (100-500 lines) | 2-5 days |
| Large (>500 lines) | 5-10 days |

---

## Coding Standards

### Python

```python
# Follow PEP 8
# Use type hints
# Use async where appropriate
# Document with docstrings

def create_trinary(value: float) -> Trinary:
    """
    Creates a trinary value from a float.

    Args:
        value: Input value to convert to trinary space.

    Returns:
        The created Trinary instance.

    Raises:
        ValueError: If value is outside valid range.
    """
    pass
```

### General Guidelines

- **DRY**: Don't Repeat Yourself
- **KISS**: Keep It Simple, Stupid
- **YAGNI**: You Aren't Gonna Need It
- **Single Responsibility**: One thing per function/class
- **Meaningful Names**: Clear, descriptive identifiers

---

## Testing Guidelines

### Test Structure

```
tests/
├── test_lucidia_logic.py
├── test_quantum.py
└── __init__.py
```

### Writing Tests

```python
def test_trinary_and_operation():
    """TRUE AND FALSE should return FALSE."""
    a = Trinary(1)   # TRUE
    b = Trinary(-1)  # FALSE
    result = a & b
    assert result.v == -1
```

### Test Coverage

| Component | Minimum Coverage |
|-----------|-----------------|
| Core logic | 80% |
| Math engines | 70% |
| Utilities | 90% |

---

## Documentation

### What to Document

- **README.md**: Project overview, quick start
- **Code comments**: Complex logic only
- **Docstrings**: All public functions

### Documentation Style

- Use clear, concise language
- Include code examples
- Keep examples up to date
- Use proper formatting

---

## Community

### Communication Channels

| Channel | Purpose |
|---------|---------|
| GitHub Issues | Bug reports, features |
| GitHub Discussions | Questions, ideas |
| Email | Private matters |

### Getting Help

1. Check existing documentation
2. Search GitHub issues
3. Open a new issue

---

## License

By contributing, you acknowledge and agree that your contributions are provided on a work-for-hire and/or assignment basis, and that all rights in your contributions are owned by BlackRoad OS, Inc., as described in Section 4 ("Contributions and Work Product") of the LICENSE file.

---

*Thank you for contributing to BlackRoad OS! 🖤🛣️*
