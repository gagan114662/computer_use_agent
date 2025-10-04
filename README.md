# Claude Code Autonomous Agent

A **fully autonomous coding agent** that takes a one-line brief, asks intelligent questions, generates a detailed PRD, and delivers 100% working code without human intervention.

## 🚀 Ultimate Workflow

```bash
./auto_prd_builder.sh 'Build a password strength validator'
```

**What happens:**
1. 🧠 Analyzes your brief intelligently
2. 💬 Asks clarifying questions (inputs, outputs, edge cases)
3. 📋 Generates comprehensive PRD
4. 👤 Shows PRD for your approval
5. 🤖 Builds project 100% autonomously
6. ✅ Delivers working code with tests - **100% correctness**

**You just verify via tests. That's it.**

## Features

- **Intelligent PRD Generation**: One-line brief → Detailed requirements
- **Smart Questioning**: Asks only what's needed based on project type
- **Fully Autonomous Development**: No babysitting needed
- **Test-Driven Development**: Writes tests first, then implements code
- **Auto-Debug**: Runs tests, finds bugs, fixes them automatically
- **Computer Control**: Can take screenshots, click, type, and control your computer
- **Zero Hardcoding**: Tests import from codebase, never duplicate logic
- **100% Correctness**: Iterates until all tests pass

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/gagan114662/computer_use_agent.git
cd computer_use_agent
```

### 2. Install Python Dependencies

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Install MCP PyAutoGUI Server

```bash
# Install the MCP server globally
pip install mcp-pyautogui
```

### 4. Configure Claude Code

Add this to your Claude Code MCP settings (`~/.config/claude-code/mcp_config.json`):

```json
{
  "mcpServers": {
    "mcp-pyautogui": {
      "command": "python",
      "args": ["-m", "mcp_pyautogui"]
    }
  }
}
```

### 5. Set Up API Keys (Optional)

For full functionality, set your Anthropic API key:

```bash
export ANTHROPIC_API_KEY="your-api-key-here"
```

### 6. Run Claude Code

```bash
claude
```

## Autonomous Development Workflow

### Method 1: Fully Automated (Recommended)

**One command does everything:**

```bash
./auto_prd_builder.sh 'Build a URL shortener'
```

**Interactive session:**
```
🤖 INTELLIGENT PRD GENERATOR

📝 Your Brief: Build a URL shortener

📋 I need some clarifications:

✓ What input types/formats will the system accept?
  → Long URLs as strings

✓ What should the outputs look like?
  → Short URL string (8 characters)

  Any specific edge cases? [Standard]
  → Invalid URLs, duplicate URLs

🔨 Generating detailed PRD...
✅ PRD saved

👤 Proceed with autonomous development? (y/N) y

🤖 Agent working autonomously...
   ✓ Writing tests FIRST (imports only)
   ✓ Implementing code
   ✓ Running pytest
   ✓ Debugging failures
   ✓ Iterating until 100% pass

✅ COMPLETE - All tests passing!
```

### Method 2: Step-by-Step Control

```bash
# Step 1: Generate PRD only
python3 interactive_prd.py 'Build a JSON validator'

# Step 2: Review/edit PRD
cat PROJECT_REQUIREMENTS.md

# Step 3: Run autonomous development
./run_autonomous.sh
```

### Method 3: Manual PRD

```bash
# 1. Create requirements manually
cp PROJECT_REQUIREMENTS.template.md PROJECT_REQUIREMENTS.md
nano PROJECT_REQUIREMENTS.md

# 2. Run autonomous agent
./run_autonomous.sh
```

### Example: What The Agent Does

Given this requirement:
```markdown
## Requirement: Calculator
- Add two numbers
- Subtract two numbers
- Handle division by zero
```

**Agent autonomously:**

1. **Writes test first** (tests/test_calculator.py):
```python
from src.calculator import add, subtract, divide
import pytest

def test_add():
    assert add(2, 3) == 5  # Imports from src, no hardcoding

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
```

2. **Implements code** (src/calculator.py):
```python
def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError
    return a / b
```

3. **Runs tests** → If fails, debugs and fixes automatically
4. **Repeats** → Until all tests pass ✅

### Interactive Mode (Manual Control)

For step-by-step control:

```bash
claude
```

Then ask Claude to:
```
Take a screenshot and tell me what you see
```

```
Click on the search bar and type "hello world"
```

```
Open my browser and search for Python tutorials
```

## File Structure

```
computer_use_agent/
├── 🚀 MAIN SCRIPTS
│   ├── auto_prd_builder.sh         # ONE COMMAND TO RULE THEM ALL
│   ├── interactive_prd.py          # Intelligent PRD generator
│   ├── prd_generator.py            # Simple PRD generator
│   └── run_autonomous.sh           # Autonomous development runner
│
├── 📋 CONFIGURATION & GUIDES
│   ├── SYSTEM_INSTRUCTIONS.md      # Core autonomous agent instructions
│   ├── USAGE_GUIDE.md              # Complete usage guide
│   ├── PROJECT_REQUIREMENTS.template.md  # Template
│   ├── PROJECT_REQUIREMENTS.example.md   # Example
│   ├── requirements.txt            # Python dependencies
│   └── mcp_config.json             # MCP server configuration
│
├── 🧪 TESTING & DEMOS
│   ├── demo_screenshot.py          # Screenshot demo
│   └── test_pyautogui_basic.py     # PyAutoGUI test
│
├── 📦 AUTO-GENERATED (by agent)
│   ├── src/                        # Your code
│   │   └── *.py
│   └── tests/                      # Your tests
│       └── test_*.py
```

## Quick Reference

### For Your Son (Simple)

```bash
# Build anything with one command
./auto_prd_builder.sh 'what you want to build'

# Answer questions
# Review PRD
# Say 'y' to proceed
# Wait for completion
# Verify: pytest tests/ -v

# Done! ✅
```

## Key Principles

### Test-Driven Development (TDD)
✅ **Tests written FIRST**
✅ **Tests import from src/** - Never duplicate logic
✅ **Tests verify behavior** - Not implementation
❌ **Never hardcode logic in tests**

### Autonomous Operation
✅ **No human intervention** - Works independently
✅ **Auto-debug** - Finds and fixes bugs
✅ **Iterative refinement** - Keeps trying until perfect
✅ **Self-verification** - Runs tests automatically

## Troubleshooting

### Permission Issues (macOS)

On macOS, you need to grant accessibility permissions:
1. Go to System Preferences → Security & Privacy → Privacy
2. Click on "Accessibility"
3. Add Terminal or your terminal app
4. Add Python

### MCP Server Not Found

Make sure the MCP server is installed:
```bash
pip install mcp-pyautogui
```

And that your config file is in the right place:
- macOS/Linux: `~/.config/claude-code/mcp_config.json`
- Windows: `%APPDATA%\claude-code\mcp_config.json`

## Requirements

- Python 3.8+
- Claude Code CLI
- macOS, Linux, or Windows
- Accessibility permissions (for screen control)

## Safety

Claude will ask for approval before:
- Executing potentially destructive commands
- Accessing files outside approved directories
- Making system-level changes

## License

MIT
