# Complete Usage Guide: Autonomous Development System

## Overview

This system takes a **one-line brief**, asks intelligent questions, generates a detailed PRD, and builds the entire project autonomously with **100% correctness**.

## The Complete Workflow

### Method 1: Fully Automated (Recommended)

```bash
./auto_prd_builder.sh 'Build a password strength validator'
```

**What happens:**
1. 🧠 System analyzes your brief
2. 💬 Asks clarifying questions interactively
3. 📋 Generates comprehensive PRD
4. 👤 Shows PRD for your approval
5. 🤖 Builds project 100% autonomously
6. ✅ Delivers working code with tests

**Example Session:**

```bash
$ ./auto_prd_builder.sh 'Build a URL shortener'

🤖 INTELLIGENT PRD GENERATOR
================================

📝 Your Brief: Build a URL shortener

🔍 Analyzing your brief...

📋 I need some clarifications to build a complete PRD:

✓ What input types/formats will the system accept?
  💡 Why: Need to define function signatures and validation
  → Long URLs as strings

✓ What should the outputs look like (format, type)?
  💡 Why: Need to define return types and test assertions
  → Short URL string (8 characters)

  Any specific edge cases or error conditions to handle? [Standard edge cases]
  → Invalid URLs, duplicate URLs

  Any performance requirements or constraints? [No specific constraints]
  → Should handle 10k URLs

🔨 Generating detailed PRD...
✅ PRD saved to PROJECT_REQUIREMENTS.md

Generated PRD:
[... shows complete PRD ...]

👤 Proceed with autonomous development? (y/N) y

🤖 Agent is now working autonomously...
   - Writing tests FIRST (imports only, no hardcoding)
   - Implementing code to pass tests
   - Running pytest automatically
   - Debugging and fixing failures
   - Iterating until 100% pass rate

[... autonomous development happens ...]

✅ DEVELOPMENT COMPLETE - 100% AUTONOMOUS

📊 Summary:
  ✓ PRD generated from one-line brief
  ✓ Code implemented autonomously
  ✓ Tests written (imports only, no hardcoding)
  ✓ All tests passing
  ✓ 100% correctness verified
```

### Method 2: Step-by-Step Control

#### Step 1: Generate PRD Only

```bash
python3 interactive_prd.py 'Build a JSON validator'
```

This will:
- Ask clarifying questions
- Generate PROJECT_REQUIREMENTS.md
- Stop for your review

#### Step 2: Review and Edit PRD

```bash
cat PROJECT_REQUIREMENTS.md
# Edit if needed
nano PROJECT_REQUIREMENTS.md
```

#### Step 3: Run Autonomous Development

```bash
./run_autonomous.sh
```

This will:
- Read PROJECT_REQUIREMENTS.md
- Build autonomously
- Run tests
- Debug and fix
- Deliver working code

### Method 3: Manual PRD Creation

```bash
# 1. Copy template
cp PROJECT_REQUIREMENTS.template.md PROJECT_REQUIREMENTS.md

# 2. Edit with your requirements
nano PROJECT_REQUIREMENTS.md

# 3. Run autonomous agent
./run_autonomous.sh
```

## Key Features

### 1. Intelligent Questioning

The system asks smart questions based on your brief:

- **Web/API projects** → Asks about endpoints, authentication
- **Data projects** → Asks about schema, storage
- **ML projects** → Asks about models, training data
- **Utilities** → Asks about inputs, outputs, edge cases

### 2. PRD Validation

Before building, the system:
- ✅ Validates all features are clearly defined
- ✅ Ensures inputs/outputs are specified
- ✅ Confirms edge cases are covered
- ✅ Verifies testing guidelines are clear

### 3. Autonomous Development

The agent works independently:
1. **Writes tests FIRST** (imports only, no hardcoding)
2. **Implements code** to pass tests
3. **Runs pytest** automatically
4. **Debugs failures** autonomously
5. **Iterates** until 100% pass rate

### 4. Quality Assurance

Every project gets:
- ✅ 100% test coverage
- ✅ All edge cases handled
- ✅ Type validation
- ✅ Error handling
- ✅ Clean, documented code

## Test Quality Rules

### ✅ CORRECT: Tests Import from Codebase

```python
# tests/test_validator.py
from src.validator import validate_password

def test_strong_password():
    # Import and test - NO hardcoding
    result = validate_password("StrongP@ss123")
    assert result == True

def test_weak_password():
    result = validate_password("weak")
    assert result == False
```

### ❌ WRONG: Hardcoded Logic in Tests

```python
# DON'T DO THIS
def test_strong_password():
    password = "StrongP@ss123"
    # Logic hardcoded in test
    has_upper = any(c.isupper() for c in password)
    has_number = any(c.isdigit() for c in password)
    result = has_upper and has_number  # WRONG!
    assert result == True
```

## Examples

### Example 1: Simple Utility

```bash
./auto_prd_builder.sh 'Build a word counter that counts words, characters, and lines'
```

Questions asked:
- Input format? → Text strings
- Output format? → Dictionary with counts
- Edge cases? → Empty strings, special characters

Result: Complete word counter with comprehensive tests

### Example 2: Data Processor

```bash
./auto_prd_builder.sh 'Create a CSV to JSON converter'
```

Questions asked:
- CSV structure? → Headers in first row
- JSON format? → Array of objects
- Error handling? → Invalid CSV, missing columns

Result: Robust converter with error handling

### Example 3: Validation Library

```bash
./auto_prd_builder.sh 'Build email and phone validator'
```

Questions asked:
- Email format? → Standard RFC 5322
- Phone formats? → US, international
- Validation rules? → Strict or lenient

Result: Complete validator with edge cases

## Verification

After development completes:

```bash
# 1. Review tests
cat tests/test_*.py

# 2. Review implementation
cat src/*.py

# 3. Run tests
source venv/bin/activate
pytest tests/ -v

# 4. Check coverage
pytest tests/ --cov=src --cov-report=term-missing

# 5. View coverage report
open htmlcov/index.html
```

## Success Criteria

Your project is complete when:
- ✅ All features from brief are implemented
- ✅ All tests pass (100%)
- ✅ Code coverage > 90%
- ✅ Tests import from codebase (no hardcoding)
- ✅ Edge cases are handled
- ✅ Error handling is robust

## Troubleshooting

### Issue: PRD Not Generated

```bash
# Check Python path
which python3

# Run with explicit Python
python3 interactive_prd.py 'your brief'
```

### Issue: Tests Not Running

```bash
# Install pytest in venv
source venv/bin/activate
pip install pytest pytest-cov

# Run tests
pytest tests/ -v
```

### Issue: Want to Modify PRD

```bash
# Edit the generated PRD
nano PROJECT_REQUIREMENTS.md

# Then run autonomous agent
./run_autonomous.sh
```

## Advanced Usage

### Custom Max Iterations

```bash
# Allow up to 100 iterations for complex projects
./run_autonomous.sh . 100
```

### Specific Project Directory

```bash
# Build in specific directory
./run_autonomous.sh ./my_project 50
```

### Integration with CI/CD

```bash
# In your CI pipeline
./auto_prd_builder.sh "$PROJECT_BRIEF" <<< "y"
pytest tests/ -v --junitxml=report.xml
```

## Tips for Best Results

1. **Be Specific in Brief**: More detail = better PRD
   - ❌ "Build a calculator"
   - ✅ "Build a scientific calculator with trig functions and memory"

2. **Answer Questions Thoughtfully**: Agent uses your answers
   - Specify exact input/output formats
   - List all edge cases you can think of
   - Mention performance needs

3. **Review PRD Before Building**: Catch issues early
   - Check all features are listed
   - Verify examples are clear
   - Ensure edge cases are covered

4. **Trust the Agent**: It will debug autonomously
   - Don't interrupt the process
   - Let it iterate until tests pass
   - Review final code, not intermediate steps

## What Your Son Can Do

```bash
# 1. One command to build anything
./auto_prd_builder.sh 'Build a markdown to HTML converter'

# 2. Answer a few questions
# → Input format?
# → Output format?
# → Edge cases?

# 3. Approve PRD
# → Review and say 'y'

# 4. Wait for completion
# → Agent builds autonomously

# 5. Verify via tests
# → Just run: pytest tests/ -v

# Done! 100% working code ✅
```

No babysitting. No debugging. Just working code.
