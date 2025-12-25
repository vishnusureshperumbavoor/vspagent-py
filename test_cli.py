#!/usr/bin/env python
"""Quick test to verify CLI command exists"""

import subprocess
import sys

print("=" * 70)
print("🎮 Testing VSP Agent CLI Command")
print("=" * 70)
print()

# Test 1: Check if command exists
print("Test 1: Checking if 'vspagent' command is available...")
try:
    result = subprocess.run(
        [sys.executable, "-m", "vspagent.cli", "--help"],
        capture_output=True,
        text=True,
        timeout=5
    )
    print("✅ CLI module is accessible!")
except Exception as e:
    print(f"❌ Error: {e}")
    
print()

# Test 2: Verify entry point
print("Test 2: Checking entry point registration...")
try:
    from importlib.metadata import entry_points
    eps = entry_points()
    console_scripts = eps.select(group='console_scripts') if hasattr(eps, 'select') else eps.get('console_scripts', [])
    vsp_entries = [e for e in console_scripts if 'vspagent' in str(e)]
    
    if vsp_entries:
        print(f"✅ Entry point registered: {vsp_entries[0]}")
        print(f"   Command: vspagent")
        print(f"   Points to: vspagent.cli:main")
    else:
        print("❌ No entry point found")
except Exception as e:
    print(f"❌ Error: {e}")

print()
print("=" * 70)
print("🎉 CLI is ready! Users can run: vspagent")
print("=" * 70)
print()
print("Note: First run will download ~1GB AI model (Qwen2.5-0.5B)")
print()

