# 🚀 VSP Agent - PyPI Deployment Guide

## 📋 Pre-requisites

1. **Create PyPI Account**
   - Go to https://pypi.org/account/register/
   - Create account and verify email
   - Enable 2FA: https://pypi.org/manage/account/
   - Create API token: https://pypi.org/manage/account/token/

2. **Install Build Tools**
```bash
pip install build twine
```

## 🔨 Build the Package

```bash
# Build distribution files
python -m build
```

This creates:
- `dist/vspagent-2.2.0-py3-none-any.whl` (wheel distribution)
- `dist/vspagent-2.2.0.tar.gz` (source distribution)

## 📤 Upload to PyPI

### First Time Upload
```bash
twine upload dist/*
```

You'll be prompted for:
- **Username**: `__token__`
- **Password**: Your PyPI API token (starts with `pypi-`)

### Upload Specific Version
```bash
twine upload dist/vspagent-2.2.0*
```

## 🧪 Test Before Publishing (Optional)

### Test on TestPyPI first
```bash
# Upload to TestPyPI
twine upload --repository testpypi dist/*

# Install from TestPyPI to test
pip install --index-url https://test.pypi.org/simple/ vspagent
```

## ✅ Verify Installation

After publishing to PyPI:

```bash
# Install from PyPI
pip install vspagent

# Test CLI
vspagent

# Test in Python
python -c "from vspagent import VSPAgent; print('Success!')"
```

## 🔄 Update Version

When releasing a new version:

1. **Update version numbers in:**
   - `setup.py` (line 6): `version="2.3.0"`
   - `vspagent/__init__.py` (line 3): `__version__ = "2.3.0"`

2. **Clean old builds:**
```bash
rm -rf build/ dist/ *.egg-info
```

3. **Build new version:**
```bash
python -m build
```

4. **Upload new version:**
```bash
twine upload dist/*
```

## 🛠️ Local Development

### Install in Editable Mode
```bash
pip install -e .
```

This installs the package in development mode, so changes to the code are immediately available.

### Test Locally
```bash
# Test CLI
vspagent

# Test imports
python -c "from vspagent import VSPAgent, biodata; print(biodata['creator'])"
```

## 📊 Monitor Package

- **PyPI Page**: https://pypi.org/project/vspagent/
- **Download Stats**: https://pypistats.org/packages/vspagent
- **Package Info**: `pip show vspagent`

## 🐛 Troubleshooting

### Error: "File already exists"
```bash
# Don't re-upload the same version. Bump version number first.
```

### Error: "Invalid credentials"
```bash
# Use __token__ as username, not your PyPI username
# Password should be your API token (pypi-...)
```

### Error: "README rendering failed"
```bash
# Check README.md syntax with:
twine check dist/*
```

## 🔐 API Token Setup

1. Go to https://pypi.org/manage/account/token/
2. Click "Add API token"
3. Give it a name (e.g., "vspagent-upload")
4. Scope: "Entire account" or "Project: vspagent"
5. Copy the token (starts with `pypi-`)
6. Save it securely!

### Save Token (Optional)
Create `~/.pypirc`:

```ini
[distutils]
index-servers =
    pypi

[pypi]
username = __token__
password = pypi-YOUR_TOKEN_HERE
```

Now you can upload without entering credentials:
```bash
twine upload dist/*
```

## 📦 Package Structure

```
vspagent-python/
├── vspagent/
│   ├── __init__.py      # Package initialization
│   ├── agent.py         # Core VSPAgent class
│   └── cli.py           # CLI interface
├── setup.py             # Package configuration
├── README.md            # Package documentation
├── LICENSE              # MIT License
├── .gitignore           # Git ignore rules
└── DEPLOYMENT_GUIDE.md  # This file
```

## 🎯 Quick Commands Reference

```bash
# Install build tools
pip install build twine

# Build package
python -m build

# Check package
twine check dist/*

# Upload to PyPI
twine upload dist/*

# Install package
pip install vspagent

# Run CLI
vspagent
```

## ✨ Success!

Your package is now live at:
```bash
pip install vspagent
```

🎉 **Congratulations on publishing to PyPI!** 🎉

