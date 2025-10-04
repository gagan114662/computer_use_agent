# Claude Code Autonomous Agent

A **fully autonomous coding agent** that takes project requirements and delivers working code without human intervention. You just verify via tests.

## Features

- **Fully Autonomous Development**: Give requirements → Get working code
- **Test-Driven Development**: Writes tests first, then implements code
- **Auto-Debug**: Runs tests, finds bugs, fixes them automatically
- **Computer Control**: Can take screenshots, click, type, and control your computer
- **No Babysitting**: Works independently until all tests pass
- **Zero Hardcoding**: Tests import from codebase, never duplicate logic

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

### The Magic: Zero-Intervention Coding

1. **You write requirements** → `PROJECT_REQUIREMENTS.md`
2. **Agent reads & understands** → Plans implementation
3. **Agent writes tests FIRST** → No hardcoding, only imports
4. **Agent implements code** → Makes tests pass
5. **Agent runs tests** → Automatically
6. **Agent debugs failures** → Fixes bugs autonomously
7. **Agent iterates** → Until all tests pass ✅
8. **You verify** → Review tests to confirm correctness

### Usage: Autonomous Mode

```bash
# 1. Create your requirements
cp PROJECT_REQUIREMENTS.template.md PROJECT_REQUIREMENTS.md
# Edit with your project requirements

# 2. Run autonomous agent
./run_autonomous.sh

# 3. Agent works independently until complete
# - Writes tests (imports only, no hardcoding)
# - Implements code
# - Runs pytest automatically
# - Debugs and fixes failures
# - Repeats until all tests pass

# 4. Verify the results
pytest tests/ -v
# Review tests in tests/ folder
# Review code in src/ folder
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
├── SYSTEM_INSTRUCTIONS.md          # Core autonomous agent instructions
├── PROJECT_REQUIREMENTS.template.md # Template for your requirements
├── PROJECT_REQUIREMENTS.example.md  # Example calculator project
├── run_autonomous.sh               # Autonomous mode runner
├── autonomous_agent.py             # Python orchestrator
├── requirements.txt                # Python dependencies
├── mcp_config.json                 # MCP server configuration
├── demo_screenshot.py              # Screenshot demo
├── test_pyautogui_basic.py        # PyAutoGUI test
│
├── src/                            # Your code goes here (auto-generated)
│   └── *.py
│
└── tests/                          # Tests go here (auto-generated)
    └── test_*.py
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
