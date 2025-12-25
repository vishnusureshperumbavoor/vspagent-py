# 🧪 Local Testing Guide - VSP Agent

## ✅ Quick Test - 3 Steps

### Step 1: Install in Development Mode
```bash
pip install -e .
```

✅ **Done!** Your package is now installed locally.

### Step 2: Run Test Suite
```bash
python test_local.py
```

✅ This tests all functionality automatically!

### Step 3: Manual Testing (Optional)
See detailed tests below.

---

## 📋 Automated Testing

### Run the Complete Test Suite
```bash
python test_local.py
```

This will test:
- ✅ Package imports
- ✅ VSPAgent class creation
- ✅ Biodata access
- ✅ GitHub integration
- ✅ Job search method
- ✅ Cover letter generator
- ✅ Chat method

**Expected Output:**
```
======================================================================
🧪 VSP Agent - Local Testing Suite
======================================================================

Test 1: Testing imports...
✅ PASS: Imports successful

Test 2: Testing VSPAgent class instantiation...
✅ PASS: VSPAgent instance created

...

======================================================================
🎉 All Tests Passed!
======================================================================
```

---

## 🔍 Manual Testing

### Test 1: Check Installation
```bash
pip show vspagent
```

**Expected output:**
```
Name: vspagent
Version: 2.2.0
Author: Vishnu Suresh Perumbavoor
Location: D:\test\vspagentpy
Editable project location: D:\test\vspagentpy
```

### Test 2: Test Imports
```bash
python -c "from vspagent import VSPAgent, biodata; print('Success!')"
```

**Expected:** `Success!`

### Test 3: Test Biodata Access
```python
python
>>> from vspagent import biodata
>>> print(biodata['creator'])
Vishnu Suresh Perumbavoor
>>> print(biodata['technologies'])
['React', 'Node.js', 'FastAPI', ...]
>>> print(biodata['socials']['github'])
https://github.com/vishnusureshperumbavoor
```

### Test 4: Test VSPAgent Class
```python
python
>>> from vspagent import VSPAgent
>>> agent = VSPAgent()
>>> print(agent.biodata['name'])
VSP Agent
```

### Test 5: Test GitHub Method
```python
>>> stats = agent.check_github()
>>> print(stats['username'])
vishnusureshperumbavoor
>>> print(stats['total_repos'])
30
```

### Test 6: Test Job Search
```python
>>> jobs = agent.search_jobs("Python Developer", "Remote")
>>> print(jobs['search_url'])
https://www.linkedin.com/jobs/search?keywords=Python+Developer&location=Remote&sortBy=DD
```

### Test 7: Test Cover Letter Generator
```python
>>> letter = agent.generate_cover_letter("SWE", "Google")
>>> print(letter[:100])
Dear Hiring Manager at Google,

I am writing to express my strong interest in the SWE position...
```

### Test 8: Test CLI Command (Optional - requires AI model download)
```bash
# Note: This will download ~1GB AI model
vspagent
```

**Expected:**
```
╔════════════════════════════════════════════════════════════╗
║          🤖  VSP Agent - Interactive Chat Mode            ║
║              Powered by Qwen2.5-0.5B AI                   ║
╚════════════════════════════════════════════════════════════╝

🚀 Initializing VSP Agent...
   🧠 Loading AI brain with Qwen2.5-0.5B...
```

---

## 🏗️ Build Testing

### Test the Build Process
```bash
# Install build tools
pip install build twine

# Build the package
python -m build

# Check the build
twine check dist/*
```

**Expected output:**
```
Checking dist/vspagent-2.2.0-py3-none-any.whl: PASSED
Checking dist/vspagent-2.2.0.tar.gz: PASSED
```

### Verify Build Artifacts
```bash
# Windows
dir dist

# Linux/Mac
ls -lh dist/
```

**Expected files:**
- `vspagent-2.2.0-py3-none-any.whl` (wheel distribution)
- `vspagent-2.2.0.tar.gz` (source distribution)

---

## 🧹 Test Installation from Build

### Method 1: Install from Wheel
```bash
pip uninstall vspagent -y
pip install dist/vspagent-2.2.0-py3-none-any.whl
python -c "from vspagent import VSPAgent; print('Wheel install works!')"
```

### Method 2: Install from Source
```bash
pip uninstall vspagent -y
pip install dist/vspagent-2.2.0.tar.gz
python -c "from vspagent import VSPAgent; print('Source install works!')"
```

---

## 🌐 Test on TestPyPI (Optional but Recommended)

Before publishing to the real PyPI, test on TestPyPI:

### Upload to TestPyPI
```bash
# Build first
python -m build

# Upload to TestPyPI
twine upload --repository testpypi dist/*
```

**Credentials:**
- Username: `__token__`
- Password: Your TestPyPI token from https://test.pypi.org/manage/account/token/

### Install from TestPyPI
```bash
# Uninstall local version
pip uninstall vspagent -y

# Install from TestPyPI
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ vspagent

# Test it
python -c "from vspagent import VSPAgent; print('TestPyPI install works!')"
```

---

## ✅ Testing Checklist

Before publishing to PyPI, verify:

- [ ] `pip install -e .` works without errors
- [ ] `python test_local.py` - All tests pass
- [ ] `python -c "from vspagent import VSPAgent, biodata"` - No errors
- [ ] `pip show vspagent` - Shows correct version (2.2.0)
- [ ] `python -m build` - Creates dist/ files successfully
- [ ] `twine check dist/*` - No errors or warnings
- [ ] GitHub integration works (check_github method)
- [ ] Job search method returns valid URLs
- [ ] Cover letter generator produces output
- [ ] README.md renders correctly on GitHub
- [ ] All files in `MANIFEST.in` are included
- [ ] Dependencies are correctly specified in `setup.py`

---

## 🐛 Troubleshooting

### Issue: Import Error
```bash
# Solution: Reinstall in editable mode
pip uninstall vspagent -y
pip install -e .
```

### Issue: Module Not Found
```bash
# Solution: Check you're in the right directory
cd D:\test\vspagentpy
pip install -e .
```

### Issue: Build Fails
```bash
# Solution: Clean and rebuild
rm -rf build/ dist/ *.egg-info  # Linux/Mac
# OR
rmdir /s build dist & del /s *.egg-info  # Windows

python -m build
```

### Issue: CLI Command Not Found
```bash
# Solution: Reinstall with console scripts
pip uninstall vspagent -y
pip install -e .
```

### Issue: Emoji Display Issues (Windows)
```bash
# Solution: Use PowerShell or update Windows Terminal
# OR run: chcp 65001 (to set UTF-8)
```

---

## 📊 Test Results Summary

After running `python test_local.py`, you should see:

```
✅ PASS: Imports successful
✅ PASS: VSPAgent instance created
✅ PASS: Biodata accessible and valid
✅ PASS: GitHub integration works
✅ PASS: Job search method works
✅ PASS: Cover letter generator works
✅ PASS: Chat method exists and handles uninitialized state

🎉 All Tests Passed!
```

---

## 🚀 Ready to Publish?

If all tests pass:

1. ✅ **Build the package:**
   ```bash
   python -m build
   ```

2. ✅ **Check the package:**
   ```bash
   twine check dist/*
   ```

3. ✅ **Upload to PyPI:**
   ```bash
   twine upload dist/*
   ```

---

## 💡 Pro Tips

1. **Always test in a clean environment:**
   ```bash
   python -m venv test_env
   source test_env/bin/activate  # Linux/Mac
   test_env\Scripts\activate     # Windows
   pip install dist/vspagent-2.2.0-py3-none-any.whl
   ```

2. **Use TestPyPI first** to catch any issues before real PyPI

3. **Test on multiple Python versions** if possible:
   ```bash
   python3.8 -m pip install -e .
   python3.9 -m pip install -e .
   python3.10 -m pip install -e .
   ```

4. **Check package size:**
   ```bash
   ls -lh dist/  # Should be reasonable size
   ```

5. **Verify all dependencies install correctly:**
   ```bash
   pip install -e .
   pip check  # Checks for dependency conflicts
   ```

---

## 📚 Additional Resources

- Python Packaging Guide: https://packaging.python.org/
- setuptools Documentation: https://setuptools.pypa.io/
- twine Documentation: https://twine.readthedocs.io/
- TestPyPI: https://test.pypi.org/

---

**✨ Happy Testing! Your package is almost ready for the world! 🌍**

