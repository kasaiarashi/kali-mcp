#!/usr/bin/env python3
"""
Kali CTF Solver MCP Server
An MCP tool for solving CTF challenges using Kali Linux tools.
"""

import asyncio
import json
import subprocess
import sys
from typing import Any, Optional
from pathlib import Path

try:
    from mcp.server import Server
    from mcp.server.stdio import stdio_server
    from mcp.types import (
        Tool,
        TextContent,
        ImageContent,
        EmbeddedResource,
        Resource,
        Prompt,
        PromptArgument,
        PromptMessage,
        GetPromptResult
    )
    import mcp.types as types
except ImportError:
    # Write to stderr, not stdout, since MCP clients expect JSON on stdout
    import sys
    sys.stderr.write("Error: mcp package not found. Install with: pip install mcp\n")
    sys.stderr.write("Try: pip install mcp\n")
    sys.stderr.flush()
    sys.exit(1)


class KaliCTFSolver:
    """Kali CTF Solver MCP Server implementation."""
    
    def __init__(self):
        self.server = Server("kali-ctf-solver")
        self.setup_tools()
        self.setup_resources()
        self.setup_prompts()
    
    def setup_tools(self):
        """Register MCP tools for CTF solving."""
        
        @self.server.list_tools()
        async def list_tools() -> list[Tool]:
            """List available CTF solving tools."""
            return [
                Tool(
                    name="execute_command",
                    description="Execute a terminal command in the Kali Linux environment. Use this for enumeration, exploitation, reverse engineering, steganography, forensics, OSINT, cryptography, and password-cracking tasks.",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "command": {
                                "type": "string",
                                "description": "The terminal command to execute (e.g., 'nmap -sV target.com', 'strings binary', 'steghide extract -sf image.jpg')"
                            },
                            "working_directory": {
                                "type": "string",
                                "description": "Optional working directory for the command (default: current directory)"
                            },
                            "timeout": {
                                "type": "integer",
                                "description": "Command timeout in seconds (default: 300)"
                            }
                        },
                        "required": ["command"]
                    }
                ),
                Tool(
                    name="analyze_file",
                    description="Analyze a file using appropriate Kali tools. Automatically detects file type and uses relevant tools (binwalk, file, strings, exiftool, etc.)",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "file_path": {
                                "type": "string",
                                "description": "Path to the file to analyze"
                            },
                            "analysis_type": {
                                "type": "string",
                                "enum": ["auto", "binary", "image", "archive", "text", "network"],
                                "description": "Type of analysis to perform (default: auto-detect)"
                            }
                        },
                        "required": ["file_path"]
                    }
                ),
                Tool(
                    name="crack_hash",
                    description="Attempt to crack a hash using hashcat or john the ripper. Supports various hash types.",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "hash": {
                                "type": "string",
                                "description": "The hash to crack"
                            },
                            "hash_type": {
                                "type": "string",
                                "description": "Hash type (e.g., 'md5', 'sha256', 'bcrypt', 'NTLM'). Use 'auto' to detect automatically."
                            },
                            "wordlist": {
                                "type": "string",
                                "description": "Path to wordlist file (default: /usr/share/wordlists/rockyou.txt)"
                            }
                        },
                        "required": ["hash"]
                    }
                ),
                Tool(
                    name="network_scan",
                    description="Perform network enumeration and scanning using nmap, gobuster, nikto, etc.",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "target": {
                                "type": "string",
                                "description": "Target IP address or hostname"
                            },
                            "scan_type": {
                                "type": "string",
                                "enum": ["port_scan", "service_scan", "vuln_scan", "web_enum", "all"],
                                "description": "Type of scan to perform"
                            },
                            "ports": {
                                "type": "string",
                                "description": "Port range or specific ports (e.g., '1-1000', '80,443,8080')"
                            }
                        },
                        "required": ["target"]
                    }
                )
            ]
        
        @self.server.call_tool()
        async def call_tool(name: str, arguments: dict[str, Any]) -> list[types.TextContent | types.ImageContent | types.EmbeddedResource]:
            """Execute a tool."""
            
            if name == "execute_command":
                return await self.execute_command(
                    arguments.get("command"),
                    arguments.get("working_directory"),
                    arguments.get("timeout", 300)
                )
            elif name == "analyze_file":
                return await self.analyze_file(
                    arguments.get("file_path"),
                    arguments.get("analysis_type", "auto")
                )
            elif name == "crack_hash":
                return await self.crack_hash(
                    arguments.get("hash"),
                    arguments.get("hash_type", "auto"),
                    arguments.get("wordlist", "/usr/share/wordlists/rockyou.txt")
                )
            elif name == "network_scan":
                return await self.network_scan(
                    arguments.get("target"),
                    arguments.get("scan_type", "all"),
                    arguments.get("ports")
                )
            else:
                raise ValueError(f"Unknown tool: {name}")
    
    def setup_resources(self):
        """Register MCP resources."""
        
        @self.server.list_resources()
        async def list_resources() -> list[Resource]:
            """List available resources."""
            return [
                Resource(
                    uri="prompt://kali-ctf-solver/instructions",
                    name="Kali CTF Solver Instructions",
                    description="Instructions for the Kali CTF Solver tool",
                    mimeType="text/markdown"
                )
            ]
        
        @self.server.read_resource()
        async def read_resource(uri: str) -> str:
            """Read a resource."""
            if uri == "prompt://kali-ctf-solver/instructions":
                prompt_file = Path(__file__).parent / "Prompt.md"
                if prompt_file.exists():
                    return prompt_file.read_text()
                return "Instructions not found."
            raise ValueError(f"Unknown resource: {uri}")
    
    def setup_prompts(self):
        """Register MCP prompts."""
        
        @self.server.list_prompts()
        async def list_prompts() -> list[Prompt]:
            """List available prompts."""
            return [
                Prompt(
                    name="kali_ctf_solver",
                    description="Activate the Kali CTF Solver persona for solving CTF challenges",
                    arguments=[
                        PromptArgument(
                            name="challenge_description",
                            description="Description of the CTF challenge to solve",
                            required=True
                        )
                    ]
                )
            ]
        
        @self.server.get_prompt()
        async def get_prompt(name: str, arguments: dict[str, str] | None) -> GetPromptResult:
            """Get a prompt."""
            if name == "kali_ctf_solver":
                prompt_file = Path(__file__).parent / "Prompt.md"
                base_prompt = prompt_file.read_text() if prompt_file.exists() else ""
                
                challenge_desc = arguments.get("challenge_description", "") if arguments else ""
                
                full_prompt = f"""{base_prompt}

## Current Challenge

{challenge_desc}

Begin solving this challenge step by step. Start with enumeration and analysis, then proceed with exploitation or analysis as appropriate."""
                
                return GetPromptResult(
                    description="Kali CTF Solver prompt",
                    messages=[
                        PromptMessage(
                            role="user",
                            content=TextContent(
                                type="text",
                                text=full_prompt
                            )
                        )
                    ]
                )
            raise ValueError(f"Unknown prompt: {name}")
    
    async def execute_command(self, command: str, working_directory: Optional[str] = None, timeout: int = 300) -> list[TextContent]:
        """Execute a terminal command safely."""
        if not command:
            return [TextContent(type="text", text="Error: No command provided")]
        
        # Safety check: prevent dangerous commands
        dangerous_patterns = [
            "rm -rf /",
            "mkfs",
            "dd if=/dev/",
            "> /dev/sd",
            "format",
            ":(){ :|:& };:"
        ]
        
        command_lower = command.lower()
        for pattern in dangerous_patterns:
            if pattern in command_lower:
                return [TextContent(
                    type="text",
                    text=f"Error: Potentially dangerous command blocked: {pattern}"
                )]
        
        try:
            # Execute command
            cwd = Path(working_directory) if working_directory else None
            
            process = await asyncio.create_subprocess_shell(
                command,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
                cwd=cwd,
                shell=True
            )
            
            stdout, stderr = await asyncio.wait_for(
                process.communicate(),
                timeout=timeout
            )
            
            output = stdout.decode('utf-8', errors='replace')
            error_output = stderr.decode('utf-8', errors='replace')
            
            result = f"""### [Command]
```bash
{command}
```

### [Result]
```
{output}
```

"""
            if error_output:
                result += f"""### [Error Output]
```
{error_output}
```

"""
            result += f"""### [Exit Code]
{process.returncode}
"""
            
            return [TextContent(type="text", text=result)]
            
        except asyncio.TimeoutError:
            return [TextContent(
                type="text",
                text=f"Error: Command timed out after {timeout} seconds"
            )]
        except Exception as e:
            return [TextContent(
                type="text",
                text=f"Error executing command: {str(e)}"
            )]
    
    async def analyze_file(self, file_path: str, analysis_type: str = "auto") -> list[TextContent]:
        """Analyze a file using appropriate Kali tools."""
        file = Path(file_path)
        
        if not file.exists():
            return [TextContent(
                type="text",
                text=f"Error: File not found: {file_path}"
            )]
        
        results = []
        
        # Auto-detect file type if needed
        if analysis_type == "auto":
            file_type_cmd = f"file '{file_path}'"
            file_type_result = await self.execute_command(file_type_cmd)
            results.extend(file_type_result)
            analysis_type = "auto"  # Keep as auto for now
        
        # Basic file info
        results.append(TextContent(
            type="text",
            text=f"### [Analysis] Analyzing file: {file_path}\n"
        ))
        
        # Use appropriate tools based on file type
        commands = []
        
        # Always get basic info
        commands.append(("file", f"file '{file_path}'"))
        commands.append(("ls", f"ls -lah '{file_path}'"))
        
        # Detect file type and add relevant commands
        if "image" in str(file).lower() or analysis_type == "image":
            commands.append(("exiftool", f"exiftool '{file_path}'"))
            commands.append(("binwalk", f"binwalk '{file_path}'"))
            commands.append(("steghide", f"steghide info '{file_path}' 2>&1 || echo 'steghide not available or no steganography detected'"))
            commands.append(("strings", f"strings '{file_path}' | head -50"))
        elif "archive" in str(file).lower() or analysis_type == "archive":
            commands.append(("binwalk", f"binwalk '{file_path}'"))
            commands.append(("7z", f"7z l '{file_path}' 2>&1 || unzip -l '{file_path}' 2>&1 || tar -tzf '{file_path}' 2>&1"))
        elif analysis_type == "binary":
            commands.append(("strings", f"strings '{file_path}'"))
            commands.append(("hexdump", f"hexdump -C '{file_path}' | head -50"))
            commands.append(("checksec", f"checksec --file='{file_path}' 2>&1 || echo 'checksec not available'"))
        else:
            # Default analysis
            commands.append(("strings", f"strings '{file_path}' | head -50"))
            commands.append(("head", f"head -20 '{file_path}'"))
        
        # Execute all commands
        for tool_name, cmd in commands:
            result = await self.execute_command(cmd)
            results.extend(result)
        
        return results
    
    async def crack_hash(self, hash_value: str, hash_type: str = "auto", wordlist: str = "/usr/share/wordlists/rockyou.txt") -> list[TextContent]:
        """Attempt to crack a hash."""
        results = []
        
        # Detect hash type if auto
        if hash_type == "auto":
            hash_len = len(hash_value)
            if hash_len == 32:
                hash_type = "md5"
            elif hash_len == 40:
                hash_type = "sha1"
            elif hash_len == 64:
                hash_type = "sha256"
            else:
                hash_type = "md5"  # Default fallback
        
        results.append(TextContent(
            type="text",
            text=f"### [Analysis] Attempting to crack {hash_type} hash: {hash_value}\n"
        ))
        
        # Try hashcat first
        hashcat_cmd = f"hashcat -m {self._get_hashcat_mode(hash_type)} '{hash_value}' '{wordlist}' --potfile-disable -o /tmp/hashcat_result.txt 2>&1 || echo 'hashcat failed or not available'"
        hashcat_result = await self.execute_command(hashcat_cmd)
        results.extend(hashcat_result)
        
        # Try john the ripper as fallback
        # Create a temporary file with the hash
        hash_file = "/tmp/hash_to_crack.txt"
        await self.execute_command(f"echo '{hash_value}' > {hash_file}")
        
        john_cmd = f"john --format={hash_type} --wordlist='{wordlist}' {hash_file} 2>&1 || echo 'john failed or not available'"
        john_result = await self.execute_command(john_cmd)
        results.extend(john_result)
        
        # Check if we got results
        check_result = await self.execute_command(f"cat /tmp/hashcat_result.txt 2>&1 || john --show --format={hash_type} {hash_file} 2>&1")
        results.extend(check_result)
        
        return results
    
    def _get_hashcat_mode(self, hash_type: str) -> str:
        """Get hashcat mode number for hash type."""
        modes = {
            "md5": "0",
            "sha1": "100",
            "sha256": "1400",
            "sha512": "1700",
            "bcrypt": "3200",
            "NTLM": "1000"
        }
        return modes.get(hash_type.lower(), "0")
    
    async def network_scan(self, target: str, scan_type: str = "all", ports: Optional[str] = None) -> list[TextContent]:
        """Perform network scanning and enumeration."""
        results = []
        
        results.append(TextContent(
            type="text",
            text=f"### [Analysis] Scanning target: {target}\n"
        ))
        
        port_arg = f"-p {ports}" if ports else ""
        
        if scan_type == "port_scan" or scan_type == "all":
            nmap_cmd = f"nmap -sS {port_arg} {target}"
            result = await self.execute_command(nmap_cmd)
            results.extend(result)
        
        if scan_type == "service_scan" or scan_type == "all":
            nmap_cmd = f"nmap -sV {port_arg} {target}"
            result = await self.execute_command(nmap_cmd)
            results.extend(result)
        
        if scan_type == "vuln_scan" or scan_type == "all":
            nmap_cmd = f"nmap --script vuln {port_arg} {target}"
            result = await self.execute_command(nmap_cmd)
            results.extend(result)
        
        if scan_type == "web_enum" or scan_type == "all":
            # Check for web services
            web_ports = ports if ports else "80,443,8080,8443"
            gobuster_cmd = f"gobuster dir -u http://{target} -w /usr/share/wordlists/dirb/common.txt 2>&1 || echo 'gobuster not available'"
            result = await self.execute_command(gobuster_cmd)
            results.extend(result)
        
        return results
    
    async def run(self):
        """Run the MCP server."""
        async with stdio_server() as (read_stream, write_stream):
            await self.server.run(
                read_stream,
                write_stream,
                self.server.create_initialization_options()
            )


def main():
    """Main entry point for the MCP server."""
    solver = KaliCTFSolver()
    asyncio.run(solver.run())


if __name__ == "__main__":
    main()

