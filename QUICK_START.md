# Quick Start Guide

## Setup (One-Time)

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Get configuration path:**
   ```bash
   ./get_path.sh
   ```

3. **Configure MCP client:**
   - Copy the path from step 2
   - Add to your MCP client config (Claude Desktop, Cursor, etc.)
   - Restart the client

## Using the Tool

### Just Talk Naturally!

The AI automatically uses the right tools when you describe what you want to do.

**Examples:**

✅ **"Scan port 80 on 192.168.1.1"**
→ Uses `network_scan` tool

✅ **"Analyze this file: mystery.bin"**
→ Uses `analyze_file` tool

✅ **"Crack this hash: 5f4dcc3b5aa765d61d8327deb882cf99"**
→ Uses `crack_hash` tool

✅ **"Run nmap -sV on 10.10.10.5"**
→ Uses `execute_command` tool

### Available Tools

| Tool | When to Use | Example Prompt |
|------|-------------|----------------|
| `execute_command` | Run any Kali command | "Run strings on binary" |
| `analyze_file` | Analyze files automatically | "Check image.jpg for hidden data" |
| `crack_hash` | Crack password hashes | "Crack this MD5 hash" |
| `network_scan` | Network enumeration | "Scan target 192.168.1.1" |

### Typical CTF Workflow

```
1. "I have a CTF challenge with [files/target]"
   → AI analyzes and suggests approach

2. "Scan the target" or "Analyze the files"
   → AI performs enumeration

3. "I found [hash/file/service]"
   → AI helps exploit/extract

4. "Get the flag"
   → AI guides you to the solution
```

## Common Commands

### Network Scanning
- "Scan ports on [target]"
- "Enumerate web directories on [url]"
- "Check for vulnerabilities on [target]"

### File Analysis
- "Analyze [file] for steganography"
- "Check what's in [binary]"
- "Extract strings from [file]"

### Hash Cracking
- "Crack this hash: [hash]"
- "Try to crack [hash] with [wordlist]"

### General Commands
- "Run [any kali command]"
- "Execute [command] in [directory]"

## Tips

1. **Be specific** - More context = better results
2. **Iterate** - Use results to guide next steps  
3. **Natural language** - No need to know exact tool names
4. **Provide context** - Mention challenge type (web, binary, forensics, etc.)

## Troubleshooting

**Tools not showing?**
- Restart MCP client
- Check config file path is correct
- Verify `kali_ctf_solver.py` is executable

**Commands failing?**
- Ensure you're in Kali Linux environment
- Check required tools are installed
- Verify file paths are correct

For detailed examples, see [USAGE_EXAMPLES.md](USAGE_EXAMPLES.md)

