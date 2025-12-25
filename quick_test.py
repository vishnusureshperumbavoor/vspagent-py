#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Quick Test Script - Run CLI Without Installation
Usage: python quick_test.py
"""

import sys
import io

# Set UTF-8 encoding for Windows console
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

print("=" * 70)
print("🚀 Quick Test - Running VSP Agent CLI Without Installation")
print("=" * 70)
print()
print("This will launch the interactive chat interface...")
print("Press Ctrl+C to exit if needed.")
print()
print("=" * 70)
print()

# Import and run the CLI
from vspagent.cli import main

# Run it!
main()

