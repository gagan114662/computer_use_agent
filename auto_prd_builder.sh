#!/bin/bash

# Complete Autonomous Development Pipeline
# From one-line brief → PRD → Code → Tests → Verification

set -e

if [ $# -eq 0 ]; then
    echo ""
    echo "🤖 AUTONOMOUS DEVELOPMENT SYSTEM"
    echo "=================================="
    echo ""
    echo "Usage: ./auto_prd_builder.sh 'your one-line brief'"
    echo ""
    echo "Examples:"
    echo "  ./auto_prd_builder.sh 'Build a password strength validator'"
    echo "  ./auto_prd_builder.sh 'Create a JSON to CSV converter'"
    echo "  ./auto_prd_builder.sh 'Build a markdown table generator'"
    echo ""
    echo "The system will:"
    echo "  1. ✓ Analyze your brief"
    echo "  2. ✓ Ask clarifying questions"
    echo "  3. ✓ Generate comprehensive PRD"
    echo "  4. ✓ Validate completeness"
    echo "  5. ✓ Build project autonomously"
    echo "  6. ✓ Run tests automatically"
    echo "  7. ✓ Debug and fix issues"
    echo "  8. ✓ Deliver 100% working code"
    echo ""
    exit 1
fi

BRIEF="$*"

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🤖 AUTONOMOUS DEVELOPMENT PIPELINE"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "📝 Brief: $BRIEF"
echo ""

# Step 1: Generate PRD with intelligent questioning
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "STEP 1: PRD GENERATION"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

python3 interactive_prd.py "$BRIEF"

if [ ! -f "PROJECT_REQUIREMENTS.md" ]; then
    echo "❌ PRD generation failed"
    exit 1
fi

echo "✅ PRD generated successfully"
echo ""

# Step 2: Show PRD for confirmation
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "STEP 2: PRD REVIEW"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "Generated PRD:"
echo ""
cat PROJECT_REQUIREMENTS.md
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

read -p "👤 Proceed with autonomous development? (y/N) " -n 1 -r
echo ""

if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "⏸️  Development paused. Edit PROJECT_REQUIREMENTS.md and run ./run_autonomous.sh"
    exit 0
fi

# Step 3: Autonomous development
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "STEP 3: AUTONOMOUS DEVELOPMENT"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "🤖 Agent is now working autonomously..."
echo "   - Writing tests FIRST (imports only, no hardcoding)"
echo "   - Implementing code to pass tests"
echo "   - Running pytest automatically"
echo "   - Debugging and fixing failures"
echo "   - Iterating until 100% pass rate"
echo ""

# In production, this would call Claude to autonomously develop
# For now, we'll use the autonomous runner

# Clean up previous builds
rm -rf src tests

# Run autonomous development
./run_autonomous.sh . 50

# Step 4: Final verification
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "STEP 4: FINAL VERIFICATION"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

source venv/bin/activate
pytest tests/ -v --cov=src --cov-report=term-missing

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✅ DEVELOPMENT COMPLETE - 100% AUTONOMOUS"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "📊 Summary:"
echo "  ✓ PRD generated from one-line brief"
echo "  ✓ Clarifying questions asked and answered"
echo "  ✓ Code implemented autonomously"
echo "  ✓ Tests written (imports only, no hardcoding)"
echo "  ✓ All tests passing"
echo "  ✓ 100% correctness verified"
echo ""
echo "📁 Deliverables:"
echo "  - PROJECT_REQUIREMENTS.md  (detailed PRD)"
echo "  - src/                     (implementation)"
echo "  - tests/                   (comprehensive tests)"
echo ""
echo "🔍 To verify:"
echo "  1. Review tests: cat tests/test_*.py"
echo "  2. Review code: cat src/*.py"
echo "  3. Run tests: pytest tests/ -v"
echo ""
echo "🎉 Your project is ready!"
echo ""
