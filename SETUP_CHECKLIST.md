# Setup Checklist

Use this checklist to ensure your Kali CTF Solver MCP tool is set up correctly.

## Pre-Setup

- [ ] Python 3.8+ installed (`python3 --version`)
- [ ] Kali Linux environment ready
- [ ] Claude Desktop or Cursor installed
- [ ] Terminal/command line access

## Installation Steps

- [ ] Navigated to project directory
- [ ] Created virtual environment (optional but recommended)
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```
- [ ] Installed dependencies
  ```bash
  pip install -r requirements.txt
  ```
- [ ] Made script executable
  ```bash
  chmod +x kali_ctf_solver.py
  ```
- [ ] Verified installation
  ```bash
  python3 -c "from mcp.server import Server; print('OK')"
  ```

## Configuration Steps

- [ ] Got absolute path to `kali_ctf_solver.py`
  ```bash
  ./get_path.sh
  # Or: realpath kali_ctf_solver.py
  ```
- [ ] Located MCP client configuration file
  - Claude Desktop: See [SETUP_GUIDE.md](SETUP_GUIDE.md) for paths
  - Cursor: See [SETUP_GUIDE.md](SETUP_GUIDE.md) for paths
- [ ] Edited configuration file
  - Added `kali-ctf-solver` entry
  - Used correct absolute path
  - Validated JSON syntax
- [ ] Saved configuration file
- [ ] Completely restarted MCP client (not just closed window)

## Verification Steps

- [ ] MCP server appears in client
- [ ] Test command works:
  ```
  "Run: echo 'Hello from Kali CTF Solver'"
  ```
- [ ] File analysis works:
  ```
  "Analyze a test file"
  ```
- [ ] No errors in MCP client logs

## Troubleshooting

If something doesn't work:

- [ ] Checked JSON syntax (`python3 -m json.tool config.json`)
- [ ] Verified file path exists and is executable
- [ ] Tested script directly (`python3 kali_ctf_solver.py`)
- [ ] Checked Python path (`which python3`)
- [ ] Verified MCP package installed (`pip list | grep mcp`)
- [ ] Checked MCP client logs for errors
- [ ] Completely quit and restarted MCP client

## Next Steps

- [ ] Read [QUICK_START.md](QUICK_START.md)
- [ ] Review [USAGE_EXAMPLES.md](USAGE_EXAMPLES.md)
- [ ] Start solving CTF challenges!

---

**Need help?** See [SETUP_GUIDE.md](SETUP_GUIDE.md) for detailed instructions and troubleshooting.

