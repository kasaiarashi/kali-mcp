# Setup Guide: Kali CTF Solver MCP Tool

This guide will walk you through setting up the Kali CTF Solver MCP tool with Claude Desktop or Cursor.

**Quick Checklist:** See [SETUP_CHECKLIST.md](SETUP_CHECKLIST.md) for a step-by-step checklist.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Step 1: Install Dependencies](#step-1-install-dependencies)
- [Step 2: Get the Configuration Path](#step-2-get-the-configuration-path)
- [Step 3: Configure Claude Desktop](#step-3-configure-claude-desktop)
- [Step 3: Configure Cursor](#step-3-configure-cursor)
- [Step 4: Verify Installation](#step-4-verify-installation)
- [Troubleshooting](#troubleshooting)

## Prerequisites

- Python 3.8 or higher installed
- Kali Linux environment (VM, container, or native)
- Claude Desktop or Cursor installed
- Terminal/command line access

## Step 1: Install Dependencies

### 1.1 Navigate to the Project Directory

```bash
cd /path/to/kali-mcp
```

### 1.2 Create Virtual Environment (Recommended)

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 1.3 Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 1.4 Make Script Executable

```bash
chmod +x kali_ctf_solver.py
```

### 1.5 Verify Installation

```bash
python3 kali_ctf_solver.py --help
# Or simply test imports:
python3 -c "from mcp.server import Server; print('MCP SDK installed successfully')"
```

If you see an error, ensure the `mcp` package is installed:
```bash
pip install mcp
```

## Step 2: Get the Configuration Path

You need the absolute path to `kali_ctf_solver.py` for the MCP client configuration.

### Option A: Using the Helper Script

```bash
./get_path.sh
```

This will output:
- The absolute path to `kali_ctf_solver.py`
- A ready-to-use JSON configuration snippet

### Option B: Manual Method

```bash
# Get the absolute path
realpath kali_ctf_solver.py
# Or on macOS/Linux:
pwd
# Then append: /kali_ctf_solver.py
```

**Example output:**
```
/Users/krishnateja/Developer/Hacking/kali-mcp/kali_ctf_solver.py
```

**Save this path** - you'll need it in the next step!

## Step 3: Configure Claude Desktop

### 3.1 Locate Claude Desktop Configuration File

The configuration file location depends on your operating system:

| OS | Configuration File Path |
|----|------------------------|
| **macOS** | `~/Library/Application Support/Claude/claude_desktop_config.json` |
| **Windows** | `%APPDATA%\Claude\claude_desktop_config.json` |
| **Linux** | `~/.config/Claude/claude_desktop_config.json` |

**Quick access commands:**

**macOS/Linux:**
```bash
# Open the directory
open ~/Library/Application\ Support/Claude/  # macOS
# Or
xdg-open ~/.config/Claude/  # Linux

# Or edit directly
nano ~/Library/Application\ Support/Claude/claude_desktop_config.json  # macOS
nano ~/.config/Claude/claude_desktop_config.json  # Linux
```

**Windows:**
```powershell
# Open in Explorer
explorer %APPDATA%\Claude

# Or edit directly
notepad %APPDATA%\Claude\claude_desktop_config.json
```

### 3.2 Edit the Configuration File

**If the file doesn't exist**, create it with this structure:

```json
{
  "mcpServers": {
    "kali-ctf-solver": {
      "command": "python3",
      "args": [
        "/absolute/path/to/kali-mcp/kali_ctf_solver.py"
      ]
    }
  }
}
```

**If the file already exists**, add `kali-ctf-solver` to the existing `mcpServers` object:

```json
{
  "mcpServers": {
    "existing-tool": {
      "command": "...",
      "args": [...]
    },
    "kali-ctf-solver": {
      "command": "python3",
      "args": [
        "/absolute/path/to/kali-mcp/kali_ctf_solver.py"
      ]
    }
  }
}
```

**Important:** Replace `/absolute/path/to/kali-mcp/kali_ctf_solver.py` with the actual path from Step 2!

### 3.3 Example Configuration

**macOS Example:**
```json
{
  "mcpServers": {
    "kali-ctf-solver": {
      "command": "python3",
      "args": [
        "/Users/krishnateja/Developer/Hacking/kali-mcp/kali_ctf_solver.py"
      ]
    }
  }
}
```

**Windows Example:**
```json
{
  "mcpServers": {
    "kali-ctf-solver": {
      "command": "python",
      "args": [
        "C:\\Users\\YourName\\kali-mcp\\kali_ctf_solver.py"
      ]
    }
  }
}
```

**Linux Example:**
```json
{
  "mcpServers": {
    "kali-ctf-solver": {
      "command": "python3",
      "args": [
        "/home/username/kali-mcp/kali_ctf_solver.py"
      ]
    }
  }
}
```

### 3.4 Validate JSON Syntax

Before saving, ensure your JSON is valid. You can validate it:

```bash
# Using Python
python3 -m json.tool claude_desktop_config.json

# Or use an online JSON validator
```

### 3.5 Restart Claude Desktop

**Important:** You must completely restart Claude Desktop for changes to take effect.

1. **Quit Claude Desktop completely** (not just close the window)
   - macOS: `Cmd + Q` or right-click dock icon → Quit
   - Windows: Close all windows and check Task Manager
   - Linux: Close all windows

2. **Reopen Claude Desktop**

3. The MCP server should now be connected

## Step 3: Configure Cursor

### 3.1 Locate Cursor MCP Configuration

Cursor's MCP configuration is typically located at:

| OS | Configuration File Path |
|----|------------------------|
| **macOS** | `~/.cursor/mcp.json` or `~/Library/Application Support/Cursor/User/globalStorage/mcp.json` |
| **Windows** | `%APPDATA%\Cursor\User\globalStorage\mcp.json` |
| **Linux** | `~/.config/Cursor/User/globalStorage/mcp.json` |

**Note:** The exact location may vary. Check Cursor's settings or documentation for the current location.

### 3.2 Access Cursor Settings

**Method 1: Via Settings UI**
1. Open Cursor
2. Go to Settings (Preferences)
3. Search for "MCP" or "Model Context Protocol"
4. Look for MCP server configuration

**Method 2: Via Command Palette**
1. Press `Cmd+Shift+P` (macOS) or `Ctrl+Shift+P` (Windows/Linux)
2. Type "MCP" or "Preferences: Open Settings"
3. Navigate to MCP configuration

**Method 3: Direct File Edit**
```bash
# macOS/Linux
nano ~/.cursor/mcp.json
# Or
nano ~/Library/Application\ Support/Cursor/User/globalStorage/mcp.json

# Windows
notepad %APPDATA%\Cursor\User\globalStorage\mcp.json
```

### 3.3 Edit the Configuration File

**If the file doesn't exist**, create it:

```json
{
  "mcpServers": {
    "kali-ctf-solver": {
      "command": "python3",
      "args": [
        "/absolute/path/to/kali-mcp/kali_ctf_solver.py"
      ]
    }
  }
}
```

**If the file already exists**, add to the `mcpServers` object:

```json
{
  "mcpServers": {
    "existing-server": {
      "command": "...",
      "args": [...]
    },
    "kali-ctf-solver": {
      "command": "python3",
      "args": [
        "/absolute/path/to/kali-mcp/kali_ctf_solver.py"
      ]
    }
  }
}
```

**Important:** Replace `/absolute/path/to/kali-mcp/kali_ctf_solver.py` with the actual path from Step 2!

### 3.4 Alternative: Cursor Settings UI

Some versions of Cursor allow configuration through the UI:

1. Open Cursor Settings
2. Navigate to "Extensions" or "MCP Servers"
3. Click "Add Server" or "+"
4. Enter:
   - **Name:** `kali-ctf-solver`
   - **Command:** `python3`
   - **Args:** `/absolute/path/to/kali-mcp/kali_ctf_solver.py`

### 3.5 Restart Cursor

1. **Completely quit Cursor** (not just close the window)
2. **Reopen Cursor**
3. The MCP server should now be available

## Step 4: Verify Installation

### 4.1 Check MCP Server Connection

**In Claude Desktop:**
1. Open Claude Desktop
2. Start a new conversation
3. Ask: "What MCP tools are available?"
4. Or try: "Help me with a CTF challenge"
5. The AI should mention Kali CTF Solver tools

**In Cursor:**
1. Open Cursor
2. Check the MCP status indicator (usually in the status bar)
3. Or open the MCP tools panel
4. You should see `kali-ctf-solver` listed

### 4.2 Test Tool Availability

Try these test prompts:

**Test 1: Basic Command**
```
"Run the command: echo 'Hello from Kali CTF Solver'"
```

**Test 2: File Analysis**
```
"Analyze a test file (create one first: echo 'test' > test.txt)"
```

**Test 3: Network Scan**
```
"Scan localhost for open ports"
```

If these work, your setup is successful!

### 4.3 Check for Errors

**In Claude Desktop:**
- Check the console/logs for MCP connection errors
- Look for error messages in the chat

**In Cursor:**
- Check the Output panel (View → Output)
- Select "MCP" from the dropdown
- Look for connection errors

## Troubleshooting

### Problem: MCP Server Not Appearing

**Solutions:**
1. **Verify JSON syntax:**
   ```bash
   python3 -m json.tool your_config_file.json
   ```

2. **Check file path:**
   ```bash
   # Verify the path exists and is executable
   ls -la /path/to/kali_ctf_solver.py
   chmod +x /path/to/kali_ctf_solver.py
   ```

3. **Test script directly:**
   ```bash
   python3 /path/to/kali_ctf_solver.py
   ```
   (It should wait for input - this is normal for MCP servers)

4. **Check Python path:**
   - Ensure `python3` is in your PATH
   - Try using full path: `/usr/bin/python3` or `/usr/local/bin/python3`

### Problem: "Command not found" or "python3 not found"

**Solutions:**
1. **Find Python:**
   ```bash
   which python3
   # Or
   which python
   ```

2. **Use full path in config:**
   ```json
   {
     "command": "/usr/bin/python3",
     "args": [...]
   }
   ```

3. **On Windows, use `python` instead of `python3`:**
   ```json
   {
     "command": "python",
     "args": [...]
   }
   ```

### Problem: "Module 'mcp' not found"

**Solutions:**
1. **Reinstall dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **If using virtual environment, ensure it's activated:**
   ```bash
   source venv/bin/activate
   pip install mcp
   ```

3. **Use full Python path with venv:**
   ```json
   {
     "command": "/path/to/kali-mcp/venv/bin/python",
     "args": [...]
   }
   ```

### Problem: Permission Denied

**Solutions:**
1. **Make script executable:**
   ```bash
   chmod +x kali_ctf_solver.py
   ```

2. **Check file permissions:**
   ```bash
   ls -la kali_ctf_solver.py
   ```

### Problem: MCP Server Starts but Tools Don't Work

**Solutions:**
1. **Check Kali Linux environment:**
   - Ensure you're running in Kali Linux
   - Verify tools are installed: `which nmap`, `which gobuster`, etc.

2. **Check MCP client logs:**
   - Look for error messages
   - Check if tools are being registered

3. **Test individual tools:**
   - Try simple commands first
   - Check if file paths are correct

### Problem: Configuration File Not Found

**Solutions:**
1. **Create the directory if it doesn't exist:**
   ```bash
   # macOS
   mkdir -p ~/Library/Application\ Support/Claude/
   
   # Linux
   mkdir -p ~/.config/Claude/
   
   # Windows (PowerShell)
   New-Item -ItemType Directory -Path "$env:APPDATA\Claude"
   ```

2. **Create the config file:**
   ```bash
   touch ~/Library/Application\ Support/Claude/claude_desktop_config.json
   ```

### Problem: Changes Not Taking Effect

**Solutions:**
1. **Completely quit and restart:**
   - Don't just close the window
   - Use Quit/Exit from menu
   - Check Task Manager/Activity Monitor for lingering processes

2. **Wait a few seconds** after restarting

3. **Check if config file was saved correctly**

### Getting Help

If you're still having issues:

1. **Check the logs:**
   - Claude Desktop: Check console output
   - Cursor: View → Output → MCP

2. **Verify each step:**
   - Dependencies installed?
   - Script executable?
   - Path correct?
   - JSON valid?
   - Client restarted?

3. **Test components individually:**
   ```bash
   # Test Python
   python3 --version
   
   # Test MCP import
   python3 -c "from mcp.server import Server; print('OK')"
   
   # Test script
   python3 kali_ctf_solver.py
   ```

## Quick Reference

### Configuration File Locations

**Claude Desktop:**
- macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
- Windows: `%APPDATA%\Claude\claude_desktop_config.json`
- Linux: `~/.config/Claude/claude_desktop_config.json`

**Cursor:**
- macOS: `~/.cursor/mcp.json` or `~/Library/Application Support/Cursor/User/globalStorage/mcp.json`
- Windows: `%APPDATA%\Cursor\User\globalStorage\mcp.json`
- Linux: `~/.config/Cursor/User/globalStorage/mcp.json`

### Configuration Template

```json
{
  "mcpServers": {
    "kali-ctf-solver": {
      "command": "python3",
      "args": [
        "/absolute/path/to/kali-mcp/kali_ctf_solver.py"
      ]
    }
  }
}
```

### Verification Commands

```bash
# Get path
./get_path.sh

# Test Python
python3 --version

# Test MCP
python3 -c "from mcp.server import Server; print('OK')"

# Test script
python3 kali_ctf_solver.py

# Validate JSON
python3 -m json.tool config_file.json
```

## Next Steps

Once setup is complete:

1. Read [QUICK_START.md](QUICK_START.md) for usage basics
2. Check [USAGE_EXAMPLES.md](USAGE_EXAMPLES.md) for detailed examples
3. Start solving CTF challenges!

Happy hacking! 🚩

