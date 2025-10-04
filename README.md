# Claude Code Autonomous Agent

A simple setup for using Claude Code CLI with computer control capabilities via MCP PyAutoGUI.

## Features

- **Computer Control**: Claude can take screenshots, click, type, and control your computer
- **Autonomous Actions**: Claude can analyze screens and decide what to do next
- **Easy Setup**: Just clone and configure

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

## What Can It Do?

Claude can now:
- Take screenshots and analyze them
- Click buttons and UI elements
- Type text into applications
- Execute keyboard shortcuts
- Scroll and navigate
- Make autonomous decisions based on what it sees

## Example Usage

In Claude Code CLI, try:

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

- `demo_screenshot.py` - Simple screenshot demo
- `test_pyautogui_basic.py` - Test PyAutoGUI installation
- `requirements.txt` - Python dependencies
- `mcp_config.json` - MCP server configuration

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
