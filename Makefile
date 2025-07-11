.PHONY: lint format sort clean type-check fix all help

# Colors for output
GREEN := \033[0;32m
YELLOW := \033[0;33m
NC := \033[0m

# Default Python interpreter
PYTHON := python3

# Linting tools paths
ISORT := $(PYTHON) -m isort
BLACK := $(PYTHON) -m black
FLAKE8 := $(PYTHON) -m flake8
MYPY := $(PYTHON) -m mypy

# Directories to lint
LINT_DIRS := backtracking binary_search dynamic_programming stack utils graphs heap linked_lists

lint: ## Run all linters
	@echo "${YELLOW}Running flake8 linter...${NC}"
	@$(FLAKE8) \
		--ignore=E501 \
		$(foreach dir,$(LINT_DIRS),$(wildcard $(dir)/**/*.py))
	@echo "${GREEN}Flake8 linting complete.${NC}"

format: ## Run code formatters
	@echo "${YELLOW}Formatting code with Black...${NC}"
	@$(BLACK) $(foreach dir,$(LINT_DIRS),$(wildcard $(dir)/**/*.py))
	@echo "${GREEN}Code formatting complete.${NC}"

sort: ## Sort imports
	@echo "${YELLOW}Sorting imports with isort...${NC}"
	@$(ISORT) $(foreach dir,$(LINT_DIRS),$(wildcard $(dir)/**/*.py))
	@echo "${GREEN}Import sorting complete.${NC}"

type-check: ## Run type checking
	@echo "${YELLOW}Running type checking...${NC}"
	@$(MYPY) $(foreach dir,$(LINT_DIRS),$(wildcard $(dir)/**/*.py)) || true
	@echo "${GREEN}Type checking complete.${NC}"

clean: ## Remove cache and temporary files
	@echo "${YELLOW}Cleaning up...${NC}"
	@find . -type d -name "__pycache__" -exec rm -rf {} +
	@find . -type f -name "*.pyc" -delete
	@find . -type f -name "*.pyo" -delete
	@find . -type f -name "*.pyd" -delete
	@echo "${GREEN}Clean up complete.${NC}"

fix: format sort ## Apply all fixes (formatting and import sorting)

all: clean lint type-check ## Run all checks and cleaning

help: ## Show this help message
	@echo "Available targets:"
	@echo "  lint       : Run flake8 linter"
	@echo "  format     : Format code with Black"
	@echo "  sort       : Sort imports with isort"
	@echo "  type-check : Run mypy type checking"
	@echo "  clean      : Remove cache and temporary files"
	@echo "  fix        : Apply formatting and import sorting"
	@echo "  all        : Run all checks and cleaning"
	@echo "  help       : Show this help message"
