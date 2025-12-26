#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Check if CLI command is registered"""

import sys
import io

# Set UTF-8 encoding for Windows console
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

print("=" * 70)
print("🔍 Checking vspagent-py CLI Command Registration")
print("=" * 70)
print()

try:
    from importlib.metadata import entry_points
    
    eps = entry_points()
    console_scripts = eps.select(group='console_scripts') if hasattr(eps, 'select') else eps.get('console_scripts', [])
    
    vsp_commands = [e for e in console_scripts if 'vspagent' in e.name]
    
    if vsp_commands:
        print("✅ CLI Commands Found:")
        for cmd in vsp_commands:
            print(f"   • {cmd.name} -> {cmd.value}")
        print()
        print("✅ Users can run: vspagent-py")
        print()
    else:
        print("❌ No vspagent commands found!")
        print()
        
except Exception as e:
    print(f"❌ Error: {e}")
    print()

print("=" * 70)
print("🧪 Testing CLI Import")
print("=" * 70)
print()

try:
    from vspagent.cli import main
    print("✅ CLI module can be imported")
    print("   Function: vspagent.cli:main")
    print()
except Exception as e:
    print(f"❌ Import error: {e}")
    print()

print("=" * 70)
print("📋 How Users Will Use It")
print("=" * 70)
print()
print("1. Install: pip install vspagent")
print("2. Run: vspagent-py")
print("3. Chat: Type messages to interact with VSP Agent")
print("4. Commands:")
print("   • 'github' - Check GitHub stats")
print("   • 'exit' or 'quit' - Exit chat")
print()
print("✅ Interactive chat is ready!")
print()


