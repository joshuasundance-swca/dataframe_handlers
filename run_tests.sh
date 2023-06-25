#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

coverage run -m pytest
coverage report
coverage html
coverage-badge -fo coverage.svg
