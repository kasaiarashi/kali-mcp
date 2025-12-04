# Troubleshooting Guide

Common issues and solutions for the Kali CTF Solver MCP tool.

## Error: "Unexpected token 'T', 'Try: pip install mcp' is not valid JSON"

### Problem
The MCP client is trying to parse error messages as JSON. This happens when:
- The `mcp` package is not installed
- The wrong Python interpreter is being used (system Python vs venv Python)

### Solution

**Option 1: Use Virtual Environment Python (Recommended)**

If you're using a virtual environment, update your MCP configuration to use the venv's Python:

```json
{
  "mcpServers": {
    "kali-ctf-solver": {
      "command": "/path/to/kali-mcp/venv/bin/python",
      "args": [
        "/path/to/kali-mcp/kali_ctf_solver.py"
      ]
    }
  }
}
```

**Option 2: Install MCP Package System-Wide**

If you prefer to use system Python:

```bash
pip3 install mcp
```

Then use `python3` in your config:

```json
{
  "mcpServers": {
    "kali-ctf-solver": {
      "command": "python3",
      "args": [
        "/path/to/kali-mcp/kali_ctf_solver.py"
      ]
    }
  }
}
```

**Option 3: Verify Installation**

Check if the package is installed:

```bash
# For venv
source venv/bin/activate
python -c "from mcp.server import Server; print('OK')"

# For system Python
python3 -c "from mcp.server import Server; print('OK')"
```

## Error: "Module 'mcp' not found"

### Problem
The `mcp` package is not installed in the Python environment being used.

### Solution

1. **Activate your virtual environment** (if using one):
   ```bash
   source venv/bin/activate
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Verify installation**:
   ```bash
   python -c "from mcp.server import Server; print('OK')"
   ```

4. **Update MCP config** to use the correct Python path (see above)

## Error: "Command not found" or "python3 not found"

### Problem
The Python interpreter path in the config is incorrect.

### Solution

1. **Find Python location**:
   ```bash
   which python3
   # Or for venv:
   which python  # (when venv is activated)
   ```

2. **Use full path in config**:
   ```json
   {
     "command": "/usr/bin/python3",
     "args": [...]
   }
   ```

3. **For venv, use venv's Python**:
   ```json
   {
     "command": "/absolute/path/to/kali-mcp/venv/bin/python",
     "args": [...]
   }
   ```

## MCP Server Not Appearing

### Problem
The MCP server doesn't show up in your client after configuration.

### Solutions

1. **Verify JSON syntax**:
   ```bash
   python3 -m json.tool your_config_file.json
   ```

2. **Check file path**:
   ```bash
   ls -la /path/to/kali_ctf_solver.py
   chmod +x /path/to/kali_ctf_solver.py
   ```

3. **Test script directly**:
   ```bash
   python3 /path/to/kali_ctf_solver.py
   ```
   (It should wait for input - this is normal)

4. **Completely restart MCP client**:
   - Don't just close the window
   - Use Quit/Exit from menu
   - Check Task Manager/Activity Monitor for lingering processes

5. **Check MCP client logs**:
   - Cursor: View → Output → Select "MCP" from dropdown
   - Claude Desktop: Check console/logs

## Permission Denied Errors

### Problem
Script cannot be executed due to permissions.

### Solution

```bash
chmod +x kali_ctf_solver.py
ls -la kali_ctf_solver.py  # Verify permissions show 'x'
```

## Virtual Environment Issues

### Problem: "venv/bin/python: No such file or directory"

### Solution

1. **Create venv if it doesn't exist**:
   ```bash
   python3 -m venv venv
   ```

2. **Activate venv**:
   ```bash
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Use correct path in config**:
   ```json
   {
     "command": "/absolute/path/to/kali-mcp/venv/bin/python",
     "args": [...]
   }
   ```

## Configuration File Not Found

### Problem
Cannot locate MCP configuration file.

### Solution

**Claude Desktop:**
- macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
- Windows: `%APPDATA%\Claude\claude_desktop_config.json`
- Linux: `~/.config/Claude/claude_desktop_config.json`

**Cursor:**
- macOS: `~/.cursor/mcp.json` or `~/Library/Application Support/Cursor/User/globalStorage/mcp.json`
- Windows: `%APPDATA%\Cursor\User\globalStorage\mcp.json`
- Linux: `~/.config/Cursor/User/globalStorage/mcp.json`

**Create directory if needed:**
```bash
# macOS Claude
mkdir -p ~/Library/Application\ Support/Claude/

# macOS Cursor
mkdir -p ~/.cursor/

# Then create the file
touch ~/Library/Application\ Support/Claude/claude_desktop_config.json
```

## Tools Not Working After Setup

### Problem
MCP server connects but tools don't execute properly.

### Solutions

1. **Verify Kali Linux environment**:
   ```bash
   which nmap
   which gobuster
   # etc.
   ```

2. **Check tool availability**:
   ```bash
   # Test a simple command
   echo "test" | python3 kali_ctf_solver.py
   ```

3. **Check MCP client logs** for specific error messages

4. **Test individual tools**:
   - Try simple commands first
   - Verify file paths are correct
   - Check permissions

## Still Having Issues?

1. **Check all components**:
   - [ ] Python 3.8+ installed
   - [ ] Virtual environment created (if using)
   - [ ] Dependencies installed (`pip install -r requirements.txt`)
   - [ ] Script is executable (`chmod +x kali_ctf_solver.py`)
   - [ ] Config file path is correct
   - [ ] JSON syntax is valid
   - [ ] Using correct Python interpreter in config
   - [ ] MCP client completely restarted

2. **Test each component**:
   ```bash
   # Test Python
   python3 --version
   
   # Test MCP import
   python3 -c "from mcp.server import Server; print('OK')"
   
   # Test script (should wait for input)
   python3 kali_ctf_solver.py
   ```

3. **Check logs**:
   - MCP client output/console
   - System logs
   - Python error messages

4. **Review setup guide**: See [SETUP_GUIDE.md](SETUP_GUIDE.md) for detailed instructions

