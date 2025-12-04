# VS Code / GitHub Copilot Setup Guide

This guide explains how to configure the Kali CTF Solver MCP tool for use with VS Code and GitHub Copilot.

## Prerequisites

- VS Code installed
- GitHub Copilot extension installed and activated
- Python 3.8+ installed
- MCP dependencies installed (see main README)

## Configuration

### Step 1: Locate or Create `.vscode/mcp.json`

The MCP configuration file should be located at:
```
.vscode/mcp.json
```

In your project root directory. If the `.vscode` folder doesn't exist, create it.

### Step 2: Configure MCP Server

Edit `.vscode/mcp.json` with the following content:

```json
{
    "mcpServers": {
        "kali-ctf-solver": {
            "command": "/absolute/path/to/kali-mcp/venv/bin/python",
            "args": [
                "/absolute/path/to/kali-mcp/kali_ctf_solver.py"
            ],
            "env": {}
        }
    }
}
```

**Important:** Replace `/absolute/path/to/kali-mcp` with your actual path.

**Example:**
```json
{
    "mcpServers": {
        "kali-ctf-solver": {
            "command": "/Users/krishnateja/Developer/Hacking/kali-mcp/venv/bin/python",
            "args": [
                "/Users/krishnateja/Developer/Hacking/kali-mcp/kali_ctf_solver.py"
            ],
            "env": {}
        }
    }
}
```

### Step 3: Get Your Path

Run this command from the project directory:

```bash
./get_path.sh
```

Or manually:
```bash
realpath kali_ctf_solver.py
```

### Step 4: Enable GitHub Copilot Agent Mode

1. **Open VS Code**
2. **Open Copilot Chat**:
   - Click the Copilot icon in the sidebar, or
   - Use shortcut: `Ctrl+Alt+I` (Windows/Linux) or `Cmd+Ctrl+I` (macOS)
3. **Switch to Agent Mode**:
   - In the Copilot Chat panel, look for the mode selector
   - Switch from "Ask" mode to **"Agent" mode**
   - Agent mode enables MCP server integration

### Step 5: Restart VS Code

**Important:** Completely restart VS Code for the MCP configuration to take effect:
- Close all VS Code windows
- Reopen VS Code
- The MCP server should now be connected

## Verification

### Test MCP Server Connection

1. **Open Copilot Chat** (in Agent mode)
2. **Ask a test question**:
   ```
   "What MCP tools are available?"
   ```
   or
   ```
   "Help me with a CTF challenge"
   ```

3. **Try a command**:
   ```
   "Run: echo 'Hello from Kali CTF Solver'"
   ```

If the tools are working, you should see responses using the Kali CTF Solver tools.

### Check MCP Status

- Look for MCP status indicators in VS Code's status bar
- Check the Output panel: View → Output → Select "MCP" from dropdown
- Look for any connection errors

## Troubleshooting

### MCP Server Not Appearing

1. **Verify JSON syntax**:
   ```bash
   python3 -m json.tool .vscode/mcp.json
   ```

2. **Check file path**:
   ```bash
   ls -la /path/to/kali_ctf_solver.py
   chmod +x /path/to/kali_ctf_solver.py
   ```

3. **Test script directly**:
   ```bash
   /path/to/venv/bin/python /path/to/kali_ctf_solver.py
   ```
   (Should wait for input - this is normal)

4. **Verify Python path**:
   ```bash
   /path/to/venv/bin/python -c "from mcp.server import Server; print('OK')"
   ```

### Agent Mode Not Available

- Ensure GitHub Copilot extension is installed and up to date
- Check that you have an active Copilot subscription
- Try restarting VS Code
- Check Copilot extension settings

### Tools Not Working

1. **Check MCP logs**:
   - View → Output → MCP
   - Look for error messages

2. **Verify dependencies**:
   ```bash
   source venv/bin/activate
   pip list | grep mcp
   ```

3. **Test Python environment**:
   ```bash
   /path/to/venv/bin/python --version
   ```

### Configuration File Location

VS Code looks for `.vscode/mcp.json` in:
- **Workspace root**: `.vscode/mcp.json` (project-specific)
- **User settings**: `~/.vscode/mcp.json` (global, if supported)

For project-specific configuration, use `.vscode/mcp.json` in your project root.

## Usage

Once configured, you can use the Kali CTF Solver tools through GitHub Copilot:

### Example Prompts

**Network Scanning:**
```
"Scan port 80 on 192.168.1.1"
```

**File Analysis:**
```
"Analyze the file mystery.bin"
```

**Hash Cracking:**
```
"Crack this MD5 hash: 5f4dcc3b5aa765d61d8327deb882cf99"
```

**General Commands:**
```
"Run nmap -sV on 10.10.10.5"
```

The AI will automatically use the appropriate MCP tools to fulfill your requests.

## Additional Resources

- [Main Setup Guide](SETUP_GUIDE.md) - Detailed setup for all platforms
- [Usage Examples](USAGE_EXAMPLES.md) - Practical usage examples
- [Quick Start](QUICK_START.md) - Quick reference guide
- [Troubleshooting](TROUBLESHOOTING.md) - Common issues and solutions

## Notes

- The `.vscode/mcp.json` file is workspace-specific
- Each VS Code workspace can have its own MCP configuration
- The configuration uses the same format as other MCP clients
- Agent mode is required for MCP server integration in GitHub Copilot

