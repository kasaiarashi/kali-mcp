#!/bin/bash
# Helper script to get the absolute path for MCP configuration

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
SOLVER_PATH="${SCRIPT_DIR}/kali_ctf_solver.py"

echo "Absolute path to kali_ctf_solver.py:"
echo "${SOLVER_PATH}"
echo ""
echo "Copy this path to your MCP client configuration file."
echo ""
echo "Example configuration entry:"
echo '{'
echo '  "mcpServers": {'
echo '    "kali-ctf-solver": {'
echo '      "command": "python3",'
echo "      \"args\": ["
echo "        \"${SOLVER_PATH}\""
echo "      ]"
echo '    }'
echo '  }'
echo '}'

