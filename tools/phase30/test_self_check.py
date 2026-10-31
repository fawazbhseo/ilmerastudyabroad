#!/usr/bin/env python3
"""Full-suite entry for temporary checker, no live request or secret fixtures."""
import pathlib,subprocess
R=pathlib.Path(__file__).resolve().parents[2]
subprocess.run(['node','tools/phase30/self_test.cjs'],cwd=R,check=True)
