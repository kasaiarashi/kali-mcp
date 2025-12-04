# Kali CTF Solver MCP Tool

An MCP (Model Context Protocol) tool for solving CTF challenges using Kali Linux tools. This tool provides AI-assisted penetration testing and CTF challenge solving capabilities.

## Features

- **Command Execution**: Execute any Kali Linux tool safely within the VM
- **File Analysis**: Automatically analyze files using appropriate tools (binwalk, strings, exiftool, etc.)
- **Hash Cracking**: Crack hashes using hashcat and John the Ripper
- **Network Scanning**: Perform network enumeration with nmap, gobuster, and other tools
- **Structured Output**: Provides clear [Analysis], [Command], and [Result] sections
- **Safety Checks**: Prevents execution of dangerous system-modifying commands

## Prerequisites

- Python 3.8 or higher
- Kali Linux environment (VM or container)
- MCP client (e.g., Claude Desktop, Cursor)

## Quick Setup

**📖 For detailed step-by-step setup instructions, see [SETUP_GUIDE.md](SETUP_GUIDE.md)**  
**✅ For a quick checklist, see [SETUP_CHECKLIST.md](SETUP_CHECKLIST.md)**

Quick setup:
1. Install dependencies: `pip install -r requirements.txt`
2. Get config path: `./get_path.sh`
3. Configure your MCP client (Claude Desktop or Cursor)
4. Restart your MCP client

## Installation

1. **Clone or download this repository**

2. **Setup Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Make the script executable**:
   ```bash
   chmod +x kali_ctf_solver.py
   ```

5. **Get the configuration path** (optional helper):
   ```bash
   ./get_path.sh
   ```
   This will show you the absolute path needed for MCP client configuration.

## Configuration

**📖 For detailed step-by-step setup instructions with screenshots and troubleshooting, see [SETUP_GUIDE.md](SETUP_GUIDE.md)**

**Setup Summary**: 
- ✅ The solver file (`kali_ctf_solver.py`) stays in this directory
- ✅ You only need to configure your MCP client (Claude Desktop, Cursor, etc.)
- ✅ The client configuration needs the absolute path to `kali_ctf_solver.py`

**Important**: The solver file (`kali_ctf_solver.py`) stays in this directory. You only need to configure your MCP client to point to it.

### Get the Absolute Path

First, get the absolute path to `kali_ctf_solver.py`:

```bash
# From the kali-mcp directory, run:
pwd
# Then append /kali_ctf_solver.py to the output
```

Or use:
```bash
realpath kali_ctf_solver.py
```

### For Claude Desktop

Edit your Claude Desktop configuration file:

- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`

Add the following to the `mcpServers` section (or merge with existing `mcpServers` if it already exists):

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

**Replace** `/absolute/path/to/kali-mcp/kali_ctf_solver.py` with the actual absolute path from the step above.

**Example** (if your directory is `/Users/krishnateja/Developer/Hacking/kali-mcp`):
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

### For Cursor

Edit your Cursor MCP configuration (typically in `~/.cursor/mcp.json` or similar):

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

**Replace** `/absolute/path/to/kali-mcp/kali_ctf_solver.py` with the actual absolute path (use `./get_path.sh` or `realpath kali_ctf_solver.py` from this directory).

**Note**: After updating the configuration, restart your MCP client (Claude Desktop, Cursor, etc.) for the changes to take effect.

## Usage

### Verifying the Setup

After configuring and restarting your MCP client, the Kali CTF Solver tools should be available. You can verify by:

1. **In Claude Desktop**: The tools will appear automatically when you mention CTF challenges or Kali Linux commands
2. **In Cursor**: The tools will be available in the MCP tools panel

### How to Use the Tools

The MCP client (Claude, Cursor AI, etc.) will automatically use these tools when you describe what you want to do. You can also explicitly request tool usage.

#### 1. **Execute Command Tool**

Use this for any Kali Linux command execution.

**Example prompts:**
- "Run nmap to scan port 80 on 192.168.1.100"
- "Execute `strings suspicious_file` to extract readable strings"
- "Use steghide to extract hidden data from image.jpg with password 'secret'"

**What it does:**
- Executes the command in your Kali Linux environment
- Returns structured output with command, results, and exit code
- Includes safety checks to prevent dangerous operations

#### 2. **Analyze File Tool**

Automatically analyzes files using appropriate Kali tools.

**Example prompts:**
- "Analyze the file `challenge.bin`"
- "Check this image file for steganography: `flag.jpg`"
- "Examine the archive file `data.tar.gz`"

**What it does:**
- Auto-detects file type
- Runs relevant tools (file, strings, binwalk, exiftool, steghide, etc.)
- Provides comprehensive analysis output

#### 3. **Crack Hash Tool**

Attempts to crack password hashes using hashcat and John the Ripper.

**Example prompts:**
- "Crack this MD5 hash: `5f4dcc3b5aa765d61d8327deb882cf99`"
- "Try to crack this SHA256 hash with the rockyou wordlist"
- "Crack this bcrypt hash: `$2a$10$...`"

**What it does:**
- Auto-detects hash type (MD5, SHA1, SHA256, etc.)
- Uses hashcat and John the Ripper
- Attempts cracking with specified or default wordlist

#### 4. **Network Scan Tool**

Performs comprehensive network enumeration.

**Example prompts:**
- "Scan the target 192.168.1.1 for open ports"
- "Perform a full service scan on 10.10.10.5"
- "Enumerate web directories on http://target.com"

**What it does:**
- Port scanning with nmap
- Service version detection
- Vulnerability scanning
- Web directory enumeration with gobuster

### Example CTF Challenge Workflow

Here's how you'd solve a typical CTF challenge:

**Challenge**: "Find the flag hidden in the provided files"

**Step 1 - Initial Analysis:**
```
You: "I have a CTF challenge with files: image.png, data.txt, and binary. Let's start by analyzing them."
```
The AI will use `analyze_file` on each file.

**Step 2 - Network Enumeration (if applicable):**
```
You: "The challenge mentions a server at 10.10.10.100. Let's scan it."
```
The AI will use `network_scan` to enumerate the target.

**Step 3 - Hash Cracking (if you find hashes):**
```
You: "I found this hash in data.txt: 098f6bcd4621d373cade4e832627b4f6. Can you crack it?"
```
The AI will use `crack_hash` to attempt cracking.

**Step 4 - Command Execution:**
```
You: "Extract the flag using steghide from image.png with the password we found"
```
The AI will use `execute_command` to run steghide.

### Direct Tool Usage (Advanced)

If your MCP client supports direct tool invocation, you can call tools directly:

**execute_command:**
```json
{
  "tool": "execute_command",
  "arguments": {
    "command": "nmap -sV 192.168.1.1",
    "timeout": 300
  }
}
```

**analyze_file:**
```json
{
  "tool": "analyze_file",
  "arguments": {
    "file_path": "/path/to/file",
    "analysis_type": "auto"
  }
}
```

**crack_hash:**
```json
{
  "tool": "crack_hash",
  "arguments": {
    "hash": "5f4dcc3b5aa765d61d8327deb882cf99",
    "hash_type": "md5"
  }
}
```

**network_scan:**
```json
{
  "tool": "network_scan",
  "arguments": {
    "target": "192.168.1.1",
    "scan_type": "all"
  }
}
```

## Tool Output Format

The tool follows a structured format:

- **[Analysis]**: Explanation of what is being done and why
- **[Command]**: The exact command being executed
- **[Result]**: The command output
- **[Result Analysis]**: Analysis of the results to decide next steps

## Safety Features

The tool includes safety checks to prevent:
- System file modifications
- Destructive commands (rm -rf /, mkfs, etc.)
- Malware installation

## Example Workflow

1. **Enumeration**: Start with network scanning or file analysis
2. **Analysis**: Review results and identify vulnerabilities or interesting findings
3. **Exploitation**: Use appropriate tools to exploit or extract information
4. **Flag Extraction**: Obtain the CTF flag

### Quick Start Example

```
You: "I have a CTF challenge with a file called mystery.bin. Help me solve it."

AI: [Automatically uses analyze_file]
     - Analyzes the binary
     - Identifies file type and extracts strings
     - Suggests next steps

You: "I see it's a Linux binary. Run it and see what it does"

AI: [Uses execute_command]
     - Runs the binary safely
     - Observes behavior
     - Provides analysis

You: "It asks for a password. The hash is 5f4dcc3b5aa765d61d8327deb882cf99"

AI: [Uses crack_hash]
     - Cracks the MD5 hash
     - Returns password
     - Suggests using it with the binary
```

For more detailed examples, see [USAGE_EXAMPLES.md](USAGE_EXAMPLES.md).

## Available Tools

- **execute_command**: Execute any terminal command
- **analyze_file**: Analyze files with appropriate tools
- **crack_hash**: Crack password hashes
- **network_scan**: Perform network enumeration

## Troubleshooting

- **Import errors**: Ensure `mcp` package is installed: `pip install mcp`
- **Permission errors**: Ensure the script is executable: `chmod +x kali_ctf_solver.py`
- **Command not found**: Ensure you're running in a Kali Linux environment with the required tools installed

## Legal and Ethical Notice

⚠️ **IMPORTANT**: This tool is intended for:
- Authorized penetration testing
- CTF competitions
- Educational purposes
- Security research with proper authorization

**NEVER** use this tool:
- On systems you don't own or have explicit written permission to test
- For unauthorized access attempts
- For any illegal activities

Always ensure you have proper authorization before performing any security testing.

## License

This project is provided as-is for educational and authorized testing purposes.

