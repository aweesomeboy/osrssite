#!/bin/bash
set -e

echo "Checking and fixing setup..."
echo ""

PROJECT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$PROJECT_DIR"

echo "Step 1: Removing corrupted .venv if present..."
if [ -d ".venv" ]; then
    rm -rf .venv
    echo "✓ Old virtual environment removed"
fi

echo ""
echo "Step 2: Running setup..."
bash setup.sh

echo ""
echo "✓ All checks passed!"
echo "You can now run the application using:"
echo "  bash run.sh"
echo ""
