#! /usr/bin/env sh
set -e

echo "Run migrations"
flask db upgrade

# Start command
exec "$@"

