# Kali CTF Solver - Usage Examples

This document provides practical examples of how to use the Kali CTF Solver MCP tool.

## Table of Contents
- [Basic Usage](#basic-usage)
- [CTF Challenge Examples](#ctf-challenge-examples)
- [Common Scenarios](#common-scenarios)
- [Troubleshooting](#troubleshooting)

## Basic Usage

### Example 1: Simple Command Execution

**Prompt:**
```
Run nmap to scan ports 1-1000 on 192.168.1.100
```

**What happens:**
- The AI uses `execute_command` tool
- Executes: `nmap -p 1-1000 192.168.1.100`
- Returns structured output with results

### Example 2: File Analysis

**Prompt:**
```
Analyze the file mystery.bin and tell me what it contains
```

**What happens:**
- The AI uses `analyze_file` tool
- Runs: `file`, `strings`, `hexdump`, `checksec` (if binary)
- Provides comprehensive analysis

### Example 3: Hash Cracking

**Prompt:**
```
I found this MD5 hash: 098f6bcd4621d373cade4e832627b4f6. Can you crack it?
```

**What happens:**
- The AI uses `crack_hash` tool
- Auto-detects MD5 hash type
- Attempts cracking with hashcat and John the Ripper
- Returns the cracked password if successful

### Example 4: Network Scanning

**Prompt:**
```
Perform a full scan on the target 10.10.10.5 including service detection and vulnerability scanning
```

**What happens:**
- The AI uses `network_scan` tool
- Runs multiple nmap scans (port scan, service scan, vuln scan)
- May also run gobuster for web enumeration
- Returns comprehensive results

## CTF Challenge Examples

### Challenge 1: Steganography

**Scenario:** You have an image file that might contain hidden data.

**Workflow:**
```
You: "I have an image file called flag.jpg. Check if it contains hidden data."

AI: [Uses analyze_file on flag.jpg]
     - Runs exiftool to check metadata
     - Runs binwalk to check for embedded files
     - Runs steghide info to check for steganography

You: "The steghide output shows there's hidden data. Extract it with password 'password123'"

AI: [Uses execute_command]
     - Runs: steghide extract -sf flag.jpg -p password123
     - Returns extracted file contents
```

### Challenge 2: Binary Analysis

**Scenario:** You have a binary file and need to find the flag.

**Workflow:**
```
You: "Analyze this binary file: challenge"

AI: [Uses analyze_file with analysis_type="binary"]
     - Runs file, strings, hexdump, checksec
     - Identifies architecture, strings, security features

You: "I see some interesting strings. Run strings again and grep for 'flag'"

AI: [Uses execute_command]
     - Runs: strings challenge | grep -i flag
     - Returns matching strings
```

### Challenge 3: Web Challenge

**Scenario:** You need to enumerate a web server.

**Workflow:**
```
You: "The challenge says there's a web server at http://10.10.10.10. Let's scan it."

AI: [Uses network_scan]
     - Scans ports 80, 443, 8080, etc.
     - Runs gobuster for directory enumeration
     - Returns discovered directories and files

You: "I see /admin directory. Let's check what's there with curl"

AI: [Uses execute_command]
     - Runs: curl http://10.10.10.10/admin
     - Returns page contents
```

### Challenge 4: Password Cracking

**Scenario:** You found a password hash and need to crack it.

**Workflow:**
```
You: "I extracted this hash from a database: 5f4dcc3b5aa765d61d8327deb882cf99. Crack it."

AI: [Uses crack_hash]
     - Detects MD5 hash
     - Runs hashcat with rockyou.txt wordlist
     - Returns cracked password: "password"

You: "Great! Now use this password to login to the service"
```

## Common Scenarios

### Scenario 1: Multi-step Enumeration

```
You: "I'm working on a CTF challenge. Start by scanning 192.168.1.50, then analyze any interesting findings."

AI: [Uses network_scan]
     - Scans target
     - Identifies open ports and services
     - Suggests next steps based on findings

You: "I see port 80 is open. Enumerate web directories."

AI: [Uses network_scan with scan_type="web_enum"]
     - Runs gobuster
     - Returns discovered directories

You: "Found /backup directory. Download and analyze backup.tar.gz"

AI: [Uses execute_command]
     - Downloads file
     - Uses analyze_file on the archive
     - Extracts and analyzes contents
```

### Scenario 2: Reverse Engineering

```
You: "I have a binary that asks for a password. Analyze it."

AI: [Uses analyze_file with analysis_type="binary"]
     - Identifies binary type
     - Extracts strings
     - Checks security features

You: "Use objdump to disassemble the main function"

AI: [Uses execute_command]
     - Runs: objdump -d binary | grep -A 50 main
     - Returns assembly code

You: "I see it compares input to a string. What's that string?"

AI: [Uses execute_command]
     - Runs: strings binary | grep -A 5 -B 5 comparison
     - Returns relevant strings
```

### Scenario 3: Forensics Challenge

```
You: "I have a disk image file.dd. Analyze it."

AI: [Uses analyze_file]
     - Identifies it as a disk image
     - Suggests mounting or using forensics tools

You: "Mount it and list the files"

AI: [Uses execute_command]
     - Mounts the image
     - Lists files
     - Identifies interesting files

You: "Check the .bash_history file for commands"

AI: [Uses execute_command]
     - Reads bash history
     - Returns command history with potential clues
```

## Tips for Effective Usage

1. **Be Specific**: The more context you provide, the better the AI can choose the right tool
   - ✅ "Scan ports 1-1000 on 192.168.1.1"
   - ❌ "Scan something"

2. **Iterate Based on Results**: Use the output to guide next steps
   - Review the [Result Analysis] sections
   - Ask follow-up questions based on findings

3. **Combine Tools**: The AI can chain multiple tools automatically
   - "Scan the target, then analyze any files you find"

4. **Use Natural Language**: You don't need to know exact tool names
   - "Check if this image has hidden data" → Uses analyze_file with steganography checks
   - "Crack this password hash" → Uses crack_hash

5. **Provide Context**: Mention what type of challenge you're working on
   - "This is a steganography challenge"
   - "I'm doing a web exploitation CTF"

## Troubleshooting

### Tool Not Available

**Problem:** The MCP client doesn't show the tools.

**Solutions:**
1. Verify configuration file path is correct
2. Restart the MCP client completely
3. Check that `kali_ctf_solver.py` is executable: `chmod +x kali_ctf_solver.py`
4. Verify Python dependencies: `pip install -r requirements.txt`

### Command Execution Fails

**Problem:** Commands return errors or don't execute.

**Solutions:**
1. Ensure you're in a Kali Linux environment
2. Check that required tools are installed (nmap, gobuster, etc.)
3. Verify file paths are correct
4. Check command syntax

### Hash Cracking Takes Too Long

**Problem:** Hash cracking seems to hang.

**Solutions:**
1. The default timeout is 300 seconds (5 minutes)
2. Large wordlists take time - be patient
3. Try specifying a smaller wordlist
4. Some hash types (bcrypt) are intentionally slow

### File Analysis Doesn't Work

**Problem:** File analysis returns errors.

**Solutions:**
1. Verify the file path is correct and absolute
2. Check file permissions
3. Ensure required tools are installed (binwalk, exiftool, etc.)
4. Try specifying analysis_type explicitly

## Advanced Usage

### Custom Wordlists

```
You: "Crack this hash using /path/to/custom_wordlist.txt"
```

### Working Directory

```
You: "Run the command in /tmp/challenge directory"
```

### Timeout Adjustment

```
You: "This command might take a while, set timeout to 600 seconds"
```

### Combining Multiple Operations

```
You: "Scan the target, analyze any files found, and crack any hashes you discover"
```

The AI will automatically chain the appropriate tools to complete the task.

