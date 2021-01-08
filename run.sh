#!/usr/bin/env bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd)"

# in .env:
# export GITHUB_USERNAME=<username>
# export GITHUB_PASSWORD=<password>

if [ -f "${DIR}/.env" ]; then
    . "$DIR/.env"
fi

if [ -z "$GITHUB_USERNAME" ]; then
    echo "Must define GITHUB_USERNAME and GITHUB_PASSWORD" && exit 1
fi

if ! command -v chromedriver >/dev/null 2>&1; then
    echo "chromedriver not found" && exit 1
fi

"${PYTHON:-python}" "${DIR}/automator.py"
