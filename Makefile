CONFIG_FILE = Makefile.config
include ${CONFIG_FILE}

PYTHON = python3
TEST_CMD = pytest

ifeq (${TEST_VERBOSE}, 1)
    TEST_CMD += $(empty) --verbose -vv
endif

ifeq (${TEST_COVERAGE}, 1)
	TEST_CMD += $(empty) --cov --cov-report=html
endif

# ===================== Help =====================

.PHONY: help
help:
	@echo "Please use 'make <target>' where <target> is one of"
	@echo ""
	@echo "  env		prepare environment and install required dependencies"
	@echo "  clean		remove all temp files"
	@echo "  clean-all	runs clean + removes the virtualenv"
	@echo "  lint		run the code linters"
	@echo "  format	    reformat code"
	@echo "  test		run all the tests"
	@echo ""
	@echo "Check the Makefile to know exactly what each target is doing."

# ===================== Setup =====================

.PHONY: env
env:
	which poetry | grep . && echo 'poetry installed' || curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3
	poetry --version
	poetry env use python3.10
	$(eval VIRTUAL_ENVS_PATH=$(shell poetry env info --path))
	@echo $(VIRTUAL_ENVS_PATH)
	poetry install
	poetry show

.PHONY: prepare
prepare: format lint test docs
	@echo "==========================="
	@echo "Ready to push your changes!"
	@echo "==========================="

# ============================== Formatting/Linting ==============================

.PHONY: lint
lint: env clean-pyc
	poetry run bash scripts/lint.sh

.PHONY: format
format: env clean-pyc

#	Format the code.
	poetry run bash scripts/format.sh

# ============================== Clean =========================================

.PHONY: clean
clean: clean-pyc

.PHONY: clean-all
clean-all: clean

clean-pyc: # Remove Python file artifacts
	find . -name '*.pyc' -exec rm -rf {} +
	find . -name '*.pyo' -exec rm -rf {} +
	find . -name '*~' -exec rm -rf {} +
	find . -name '__pycache__' -exec rm -fr {} +
# ==============================================================================