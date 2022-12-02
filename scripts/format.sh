#!/usr/bin/env bash

set -e
set -x

black  main.py viz.py
isort  main.py viz.py