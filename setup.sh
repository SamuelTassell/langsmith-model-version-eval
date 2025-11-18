#!/bin/bash

# Quick setup script for the LangSmith Model Evaluation project
# This script sets up the virtual environment and installs dependencies

echo "🚀 Setting up LangSmith Model Version Evaluation..."
echo ""

# Check Python version
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is not installed."
    echo "Please install Python 3.8 or higher and try again."
    exit 1
fi

PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
echo "✓ Found Python $PYTHON_VERSION"

# Create virtual environment
echo ""
echo "📦 Creating virtual environment..."
python3 -m venv venv

if [ $? -ne 0 ]; then
    echo "❌ Failed to create virtual environment"
    exit 1
fi
echo "✓ Virtual environment created"

# Activate virtual environment
echo ""
echo "🔌 Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo ""
echo "⬆️  Upgrading pip..."
pip install --upgrade pip -q

if [ $? -ne 0 ]; then
    echo "❌ Failed to upgrade pip"
    exit 1
fi
echo "✓ pip upgraded"

# Install dependencies
echo ""
echo "📥 Installing dependencies (this may take a few minutes)..."
pip install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "❌ Failed to install dependencies"
    exit 1
fi
echo "✓ Dependencies installed"

# Setup .env file if it doesn't exist
echo ""
if [ ! -f .env ]; then
    echo "📝 Creating .env file from template..."
    cp .env.example .env
    echo "✓ .env file created"
    echo ""
    echo "⚠️  IMPORTANT: Please edit .env and add your API keys:"
    echo "   - LANGCHAIN_API_KEY"
    echo "   - OPENAI_API_KEY"
else
    echo "✓ .env file already exists"
fi

# Success message
echo ""
echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "1. Edit .env file and add your API keys (if not already done)"
echo "2. Activate the virtual environment: source venv/bin/activate"
echo "3. Start Jupyter: jupyter notebook"
echo "4. Open notebooks/model_evaluation.ipynb"
echo ""
echo "To deactivate the virtual environment later, run: deactivate"
