#!/usr/bin/env bash

set -e
set -x

mypy app.py src/*.py src/**/*.py tests/*.py tests/**/*.py
flake8 tests src app.py
black tests src app.py --check --diff
isort tests src app.py --check-only