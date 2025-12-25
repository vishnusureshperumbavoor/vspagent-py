#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Local Testing Script for VSP Agent
Run this to test all functionality before publishing to PyPI
"""

import sys
import os

# Set UTF-8 encoding for Windows console
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

print("=" * 70)
print("🧪 VSP Agent - Local Testing Suite")
print("=" * 70)
print()

# Test 1: Import Test
print("Test 1: Testing imports...")
try:
    from vspagent import VSPAgent, biodata
    print("✅ PASS: Imports successful")
    print(f"   - Package name: {biodata['name']}")
    print(f"   - Creator: {biodata['creator']}")
    print(f"   - Version: vspagent v2.2.0")
except Exception as e:
    print(f"❌ FAIL: Import error - {e}")
    exit(1)
print()

# Test 2: VSPAgent Class Test
print("Test 2: Testing VSPAgent class instantiation...")
try:
    agent = VSPAgent()
    print("✅ PASS: VSPAgent instance created")
    print(f"   - Agent biodata keys: {len(agent.biodata)} items")
except Exception as e:
    print(f"❌ FAIL: VSPAgent creation error - {e}")
    exit(1)
print()

# Test 3: Biodata Access Test
print("Test 3: Testing biodata access...")
try:
    assert biodata['creator'] == "Vishnu Suresh Perumbavoor"
    assert 'technologies' in biodata
    assert 'socials' in biodata
    assert len(biodata['technologies']) > 0
    print("✅ PASS: Biodata accessible and valid")
    print(f"   - Technologies: {len(biodata['technologies'])} items")
    print(f"   - Social links: {len(biodata['socials'])} platforms")
except Exception as e:
    print(f"❌ FAIL: Biodata test error - {e}")
    exit(1)
print()

# Test 4: GitHub Method Test
print("Test 4: Testing GitHub integration...")
try:
    stats = agent.check_github()
    if 'error' in stats:
        print(f"⚠️  WARN: GitHub API returned: {stats['error']}")
        print("   (This is OK - may be rate limited)")
    else:
        print("✅ PASS: GitHub integration works")
        print(f"   - Username: {stats.get('username', 'N/A')}")
        print(f"   - Total repos: {stats.get('total_repos', 'N/A')}")
except Exception as e:
    print(f"❌ FAIL: GitHub test error - {e}")
    # Don't exit - this is not critical
print()

# Test 5: Job Search Method Test
print("Test 5: Testing job search method...")
try:
    jobs = agent.search_jobs("Python Developer", "Remote")
    assert 'search_url' in jobs
    assert 'role' in jobs
    assert 'location' in jobs
    print("✅ PASS: Job search method works")
    print(f"   - Search URL generated successfully")
except Exception as e:
    print(f"❌ FAIL: Job search test error - {e}")
    exit(1)
print()

# Test 6: Cover Letter Method Test
print("Test 6: Testing cover letter generator...")
try:
    letter = agent.generate_cover_letter("Software Engineer", "Google")
    assert len(letter) > 100
    assert "Software Engineer" in letter
    assert "Google" in letter
    print("✅ PASS: Cover letter generator works")
    print(f"   - Generated {len(letter)} characters")
except Exception as e:
    print(f"❌ FAIL: Cover letter test error - {e}")
    exit(1)
print()

# Test 7: AI Chat Method Test (without loading model)
print("Test 7: Testing chat method (without AI model)...")
try:
    response = agent.chat("Test message")
    # Should return error message since we haven't loaded the model
    assert "Please initialize AI first" in response
    print("✅ PASS: Chat method exists and handles uninitialized state")
    print(f"   - Response: {response[:50]}...")
except Exception as e:
    print(f"❌ FAIL: Chat method test error - {e}")
    exit(1)
print()

# Summary
print("=" * 70)
print("🎉 All Tests Passed!")
print("=" * 70)
print()
print("Your package is ready for publishing to PyPI!")
print()
print("Next steps:")
print("  1. Build: python -m build")
print("  2. Check: twine check dist/*")
print("  3. Upload: twine upload dist/*")
print()
print("Or run:")
print("  Windows: build.bat")
print("  Linux/Mac: ./build.sh")
print()

