# 🚀 VSP Agent - Quick Start Guide

## ✅ Project Setup Complete!

Your Python package is ready to be published to PyPI!

## 📁 Project Structure

```
vspagent-python/
├── vspagent/               # Main package directory
│   ├── __init__.py        # Package initialization (v2.2.0)
│   ├── agent.py           # VSPAgent class with AI functionality
│   └── cli.py             # Command-line interface
├── setup.py               # PyPI package configuration
├── README.md              # Package documentation
├── LICENSE                # MIT License
├── .gitignore            # Git ignore rules
├── DEPLOYMENT_GUIDE.md    # Detailed deployment instructions
├── QUICK_START.md         # This file
├── build.bat              # Windows build script
└── build.sh               # Linux/Mac build script
```

## 🎯 Next Steps

### Option 1: Quick Build (Windows)
```cmd
build.bat
```

### Option 2: Quick Build (Linux/Mac)
```bash
chmod +x build.sh
./build.sh
```

### Option 3: Manual Build
```bash
# Install tools
pip install build twine

# Build package
python -m build

# Check package
twine check dist/*

# Upload to PyPI
twine upload dist/*
```

## 🧪 Test Locally First

```bash
# Install in development mode
pip install -e .

# Test the CLI
vspagent

# Test in Python
python
>>> from vspagent import VSPAgent, biodata
>>> print(biodata['creator'])
Vishnu Suresh Perumbavoor
>>> agent = VSPAgent()
>>> agent.check_github()
```

## 📤 Publishing to PyPI

### 1. Create PyPI Account
- Go to https://pypi.org/account/register/
- Verify your email
- Enable 2FA
- Create an API token

### 2. Build the Package
```bash
python -m build
```

### 3. Upload to PyPI
```bash
twine upload dist/*
```

When prompted:
- **Username**: `__token__`
- **Password**: Your PyPI API token (pypi-...)

### 4. Verify Publication
```bash
pip install vspagent
vspagent
```

## 🎉 Success!

Once published, anyone can install your package:

```bash
pip install vspagent
```

## 📊 Package Features

### CLI Usage
```bash
vspagent                    # Start interactive chat
```

Commands in CLI:
- Chat with the AI naturally
- Type `github` - Check GitHub stats
- Type `exit` - Quit the program

### Python API Usage
```python
from vspagent import VSPAgent, biodata

# Create and initialize agent
agent = VSPAgent()
agent.init_ai()

# Chat
response = agent.chat("Tell me about VSP")
print(response)

# Check GitHub
stats = agent.check_github()
print(f"Repos: {stats['total_repos']}")

# Search jobs
jobs = agent.search_jobs("Python Developer", "Remote")
print(jobs['search_url'])

# Generate cover letter
letter = agent.generate_cover_letter("SWE", "Google")
print(letter)

# Access biodata
print(biodata['technologies'])
print(biodata['socials']['linkedin'])
```

## 🔄 Update Package Version

1. Edit `setup.py` and `vspagent/__init__.py`
2. Change version to `"2.3.0"` (or next version)
3. Clean old builds: `rm -rf dist/ build/ *.egg-info`
4. Build: `python -m build`
5. Upload: `twine upload dist/*`

## 🔗 Important Links

- **PyPI Project**: https://pypi.org/project/vspagent/
- **GitHub Repo**: https://github.com/vishnusureshperumbavoor/vsp_bot
- **LinkedIn**: https://www.linkedin.com/in/vishnu-suresh-perumbavoor/

## 📚 Documentation

For detailed instructions, see:
- `DEPLOYMENT_GUIDE.md` - Complete deployment guide
- `README.md` - Package documentation

## 💡 Tips

1. **Test on TestPyPI first** (optional but recommended):
   ```bash
   twine upload --repository testpypi dist/*
   ```

2. **Save your PyPI token** in `~/.pypirc`:
   ```ini
   [pypi]
   username = __token__
   password = pypi-YOUR_TOKEN_HERE
   ```

3. **Check package before upload**:
   ```bash
   twine check dist/*
   ```

4. **View package info**:
   ```bash
   pip show vspagent
   ```

## 🐛 Troubleshooting

### "File already exists"
→ Bump the version number in `setup.py` and `__init__.py`

### "Invalid credentials"
→ Username must be `__token__`, not your PyPI username

### "README rendering failed"
→ Run `twine check dist/*` to see the issue

### "Module not found"
→ Run `pip install transformers torch requests`

## ✨ You're Ready!

Your VSP Agent package is complete and ready for PyPI! 🎉

Happy Publishing! 🚀

