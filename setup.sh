#!/bin/bash
# Setup script for Kali CTF Solver MCP Tool

echo "Setting up Kali CTF Solver MCP Tool..."

# Check Python version
if ! command -v python3 &> /dev/null; then
    echo "Error: python3 is not installed"
    exit 1
fi

# Check if we're in a Kali Linux environment (optional check)
if [ -f /etc/os-release ]; then
    if grep -qi "kali" /etc/os-release; then
        echo "✓ Detected Kali Linux environment"
    else
        echo "⚠ Warning: Not running in Kali Linux. Some tools may not be available."
    fi
else
    echo "⚠ Warning: Could not detect OS. Ensure you're in a Kali Linux environment."
fi

# Install Python dependencies
echo "Installing Python dependencies..."
pip3 install -r requirements.txt

# Make script executable
chmod +x kali_ctf_solver.py

echo ""
echo "✓ Setup complete!"
echo ""
echo "Next steps:"
echo "1. Configure your MCP client (see README.md)"
echo "2. Update the path in mcp_config_example.json"
echo "3. Restart your MCP client"
echo ""
echo "To test the server, run:"
echo "  python3 kali_ctf_solver.py"

