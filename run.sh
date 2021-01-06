#!/usr/bin/env bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd)"

# in .env:
# export GITHUB_USERNAME=<username>
# export GITHUB_PASSWORD=<password>

if [ -f "${DIR}/.env" ]; then
    . "$DIR/.env"
fi

python automator.py
