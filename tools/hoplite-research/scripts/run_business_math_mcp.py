"""Launch the local arithmetic MCP with the project's isolated environment."""

import argparse
import os

from mcp_runtime import ROOT, isolated_environment


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()
    python = ROOT / ".venv" / "bin" / "python"
    if not python.is_file():
        parser.error("Dependencies are not installed. Run: bash .hoplite/setup.sh")
    os.chdir(ROOT)
    os.execve(python, [str(python), "-B", str(ROOT / "scripts" / "business_math_mcp.py")],
              isolated_environment())


if __name__ == "__main__":
    main()
