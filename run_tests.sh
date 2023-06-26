#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

coverage run -m pytest
coverage report --format markdown --no-skip-covered --skip-empty --show-missing > COVERAGE.md
coverage-badge -fo coverage.svg
