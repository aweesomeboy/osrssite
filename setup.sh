#!/bin/bash
set -e

echo "OSRS Profit Advisor Setup Script"
echo "=================================="

# Check Python version
PYTHON_CMD="python3"
if ! command -v python3 &> /dev/null; then
    if command -v python &> /dev/null; then
        PYTHON_CMD="python"
    else
        echo "❌ Error: Python 3 is required but not found."
        exit 1
    fi
fi

echo "✓ Found Python"

# Creating fresh virtual environment
echo "[1/4] Creating fresh virtual environment..."
$PYTHON_CMD -m venv .venv
echo "✓ Virtual environment created"

# Activating virtual environment
echo "[2/4] Activating virtual environment..."
if [ -f ".venv/bin/activate" ]; then
    source .venv/bin/activate
    echo "✓ Virtual environment activated"
else
    echo "❌ Error: Activation script not found."
    exit 1
fi

# Installing dependencies
echo "[3/4] Installing dependencies..."
pip install --upgrade pip setuptools wheel
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
    echo "✓ Dependencies installed"
else
    # Install defaults if requirements is missing
    pip install fastapi uvicorn httpx pydantic watchfiles uvloop websockets
    echo "✓ Installed default dependencies"
fi

# Permissions fix
echo "[4/4] Setting proper user permissions..."
chmod +x run.sh fix-setup.sh 2>/dev/null || true
echo "✓ Permissions updated"

echo ""
echo "Setup complete! You can now run the app using:"
echo "  bash run.sh"
echo ""
