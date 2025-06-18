# LeetCode Problem Solutions

## Project Setup and Development

### Prerequisites

- Python 3.8+
- `pip` package manager
- `venv` or `virtualenv`
- `make` utility

### Environment Setup

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Code Quality and Linting

#### Makefile Commands

The project provides several `make` commands for code quality:

- `make lint`: Run flake8 linter
- `make format`: Apply Black code formatting
- `make sort`: Sort imports with isort
- `make type-check`: Run mypy type checking
- `make clean`: Remove cache and temporary files
- `make fix`: Apply formatting and import sorting
- `make all`: Run comprehensive code checks
- `make help`: Show available commands

Example usage:
```bash
# Run all linting and checks
make all

# Quick fix formatting and imports
make fix

# Just run linters
make lint
```

### Running Tests

```bash
pytest
```

## Contributing

1. Create a new branch
2. Write code
3. Run `make all` to ensure code quality
4. Submit a pull request