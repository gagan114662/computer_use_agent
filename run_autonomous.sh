#!/bin/bash

# Autonomous Agent Runner for Claude Code
# This script manages the autonomous development loop

set -e

PROJECT_DIR="${1:-.}"
MAX_ITERATIONS=${2:-50}

echo "🤖 Claude Code Autonomous Agent"
echo "================================"
echo ""
echo "Project: $PROJECT_DIR"
echo "Max iterations: $MAX_ITERATIONS"
echo ""

# Check requirements file exists
if [ ! -f "$PROJECT_DIR/PROJECT_REQUIREMENTS.md" ]; then
    echo "❌ Error: PROJECT_REQUIREMENTS.md not found"
    echo ""
    echo "Create requirements file first:"
    echo "  cp PROJECT_REQUIREMENTS.template.md PROJECT_REQUIREMENTS.md"
    echo "  # Edit with your requirements"
    exit 1
fi

# Create project structure
mkdir -p "$PROJECT_DIR/src"
mkdir -p "$PROJECT_DIR/tests"
touch "$PROJECT_DIR/src/__init__.py"
touch "$PROJECT_DIR/tests/__init__.py"

echo "✅ Project structure ready"
echo ""

# Read system instructions
SYSTEM_INSTRUCTIONS=$(cat SYSTEM_INSTRUCTIONS.md)
REQUIREMENTS=$(cat "$PROJECT_DIR/PROJECT_REQUIREMENTS.md")

# Create initial prompt
INITIAL_PROMPT="AUTONOMOUS MODE: Implement the following requirements using TDD.

SYSTEM INSTRUCTIONS:
$SYSTEM_INSTRUCTIONS

PROJECT REQUIREMENTS:
$REQUIREMENTS

INSTRUCTIONS:
1. Write tests FIRST in tests/ folder (import from src/, NO hardcoding)
2. Implement code in src/ folder to make tests pass
3. Run tests: pytest tests/ -v
4. If tests fail, debug and fix automatically
5. Repeat until all tests pass

Begin implementation now. Work autonomously until complete."

# Start autonomous loop
echo "🚀 Starting autonomous development..."
echo ""

for ((i=1; i<=MAX_ITERATIONS; i++)); do
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "ITERATION $i/$MAX_ITERATIONS"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""

    # Run tests
    if pytest "$PROJECT_DIR/tests/" -v --tb=short 2>&1 | tee test_output.log; then
        echo ""
        echo "✅ ALL TESTS PASSED!"
        echo ""

        # Generate coverage report
        pytest "$PROJECT_DIR/tests/" --cov="$PROJECT_DIR/src" --cov-report=term --cov-report=html

        echo ""
        echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
        echo "✅ DEVELOPMENT COMPLETE"
        echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
        echo ""
        echo "Iterations used: $i"
        echo "Coverage report: htmlcov/index.html"
        echo ""
        echo "To verify:"
        echo "  1. Review tests in tests/ folder"
        echo "  2. Review code in src/ folder"
        echo "  3. Run: pytest tests/ -v"
        echo ""

        exit 0
    fi

    # Tests failed - prepare debug prompt
    TEST_OUTPUT=$(cat test_output.log)

    DEBUG_PROMPT="AUTONOMOUS DEBUGGING - Iteration $i

Test results:
$TEST_OUTPUT

INSTRUCTIONS:
1. Analyze the error carefully
2. Identify the bug in src/ code (DO NOT modify tests)
3. Fix the code
4. Tests will run automatically next iteration

Fix the issue now autonomously."

    echo ""
    echo "❌ Tests failed. Analyzing and fixing..."
    echo ""

    # In production, send to Claude API here
    # For now, this is a placeholder showing where Claude would fix the code

    # echo "$DEBUG_PROMPT" | claude chat --continue

    # Simulated delay (in production, Claude would be working)
    sleep 2
done

echo ""
echo "❌ Maximum iterations ($MAX_ITERATIONS) reached"
echo "Development incomplete. Manual intervention required."
exit 1
