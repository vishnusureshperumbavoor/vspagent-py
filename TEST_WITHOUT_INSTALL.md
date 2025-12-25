# 🧪 Test VSP Agent Without pip install

## 🎯 Quick Testing Methods

You can test your `vspagent-py` CLI **directly from source code** without any pip installation!

---

## ✅ Method 1: Run as Python Module (Best!)

From your project directory:

```bash
python -m vspagent.cli
```

**What this does:**
- Runs `vspagent/cli.py` directly
- No installation needed
- Uses your local source code
- Perfect for testing changes

**Example:**
```bash
D:\test\vspagentpy> python -m vspagent.cli

╔════════════════════════════════════════════════════════════╗
║          🤖  VSP Agent - Interactive Chat Mode            ║
║              Powered by Qwen2.5-0.5B AI                   ║
╚════════════════════════════════════════════════════════════╝

🚀 Initializing VSP Agent...
💬 You: [Start chatting!]
```

---

## ✅ Method 2: Run File Directly

```bash
python vspagent/cli.py
```

**What this does:**
- Runs the CLI file directly
- Even simpler than Method 1
- No pip install needed

---

## ✅ Method 3: Create a Test Script

Create `test_chat.py`:

```python
#!/usr/bin/env python
"""Quick test script for CLI chat"""

from vspagent.cli import main

if __name__ == "__main__":
    main()
```

Then run:
```bash
python test_chat.py
```

---

## ✅ Method 4: Interactive Python Session

Test the agent programmatically:

```bash
python
```

Then in Python:
```python
>>> from vspagent import VSPAgent
>>> agent = VSPAgent()
>>> agent.init_ai()  # This will download model first time

🚀 Initializing VSP Agent...
   🧠 Loading AI brain with Qwen2.5-0.5B...
✅ VSP Agent is ready!

>>> # Now chat!
>>> response = agent.chat("Who is VSP?")
>>> print(response)

VSP stands for Vishnu Suresh Perumbavoor...

>>> # Check GitHub
>>> stats = agent.check_github()
>>> print(stats)

{'username': 'vishnusureshperumbavoor', 'total_repos': 30, ...}

>>> # Exit
>>> exit()
```

---

## 🔧 Testing Individual Features

### Test 1: Test Imports
```bash
python -c "from vspagent import VSPAgent, biodata; print('✅ Imports work!')"
```

### Test 2: Test Biodata
```bash
python -c "from vspagent import biodata; print(biodata['creator'])"
```

### Test 3: Test Agent Creation
```bash
python -c "from vspagent import VSPAgent; a = VSPAgent(); print('✅ Agent created!')"
```

### Test 4: Test GitHub Method (No AI needed)
```bash
python -c "from vspagent import VSPAgent; a = VSPAgent(); print(a.check_github())"
```

### Test 5: Test CLI Import
```bash
python -c "from vspagent.cli import main; print('✅ CLI can be imported')"
```

---

## 🚀 Full Test Sequence (No Installation)

Run these commands one by one from your project directory:

```bash
# Test 1: Check structure
ls vspagent/

# Test 2: Test imports
python -c "from vspagent import VSPAgent, biodata; print('✅ OK')"

# Test 3: Test agent
python -c "from vspagent import VSPAgent; VSPAgent(); print('✅ OK')"

# Test 4: Run automated tests
python test_local.py

# Test 5: Run CLI directly (THE MAIN TEST!)
python -m vspagent.cli
```

---

## 💡 Best Practice: Use Method 1

**For daily testing during development:**

```bash
# Make changes to your code
# Then immediately test:
python -m vspagent.cli
```

**Benefits:**
- ✅ No installation needed
- ✅ Tests latest code changes
- ✅ Fast iteration
- ✅ Same as production CLI experience

---

## 🎯 When to Use Each Method

| Method | Use When |
|--------|----------|
| `python -m vspagent.cli` | Testing CLI interface |
| `python vspagent/cli.py` | Quick CLI test |
| `test_chat.py` | Custom test scenarios |
| Interactive Python | Testing API/methods |
| `test_local.py` | Full automated testing |

---

## 🔄 Development Workflow

### 1. Make Changes
Edit files in `vspagent/`:
- `agent.py` - Core logic
- `cli.py` - CLI interface

### 2. Test Immediately
```bash
python -m vspagent.cli
```

### 3. Iterate
- Make more changes
- Test again
- Repeat until satisfied

### 4. Run Full Tests
```bash
python test_local.py
```

### 5. Only Then Install
```bash
pip install -e .  # Editable install
# OR
python -m build   # Build for PyPI
```

---

## 🐛 Troubleshooting

### Issue: "No module named vspagent"
**Solution:** Make sure you're in the project directory
```bash
cd D:\test\vspagentpy
python -m vspagent.cli
```

### Issue: "transformers not found"
**Solution:** Install dependencies
```bash
pip install transformers torch requests
python -m vspagent.cli
```

### Issue: Model download fails
**Solution:** Ensure internet connection for first run
```bash
# Model downloads to: ~/.cache/huggingface/
```

---

## 📊 Comparison: Testing Methods

### Without Installation (Recommended for Development)
```bash
python -m vspagent.cli
```
- ✅ Instant testing
- ✅ No installation overhead
- ✅ Tests latest code
- ✅ Easy to iterate
- ❌ Can't test `vspagent-py` command name

### With pip install -e (Editable Mode)
```bash
pip install -e .
vspagent-py
```
- ✅ Tests actual command
- ✅ Tests installation
- ✅ Tests entry points
- ✅ Code changes still reflected
- ⚠️ One-time install needed

### With pip install (Production)
```bash
pip install .
vspagent-py
```
- ✅ Tests exactly as users will use it
- ✅ Full production test
- ❌ Need to reinstall after changes
- ❌ Slower iteration

---

## 🎯 Quick Reference

**Just want to test chat right now?**

```bash
# Step 1: Go to project directory
cd D:\test\vspagentpy

# Step 2: Run CLI directly
python -m vspagent.cli

# Step 3: Start chatting!
💬 You: Tell me about VSP
```

**That's it!** No pip install needed! 🎉

---

## 💻 Example Session

```bash
D:\test\vspagentpy> python -m vspagent.cli

╔════════════════════════════════════════════════════════════╗
║          🤖  VSP Agent - Interactive Chat Mode            ║
║              Powered by Qwen2.5-0.5B AI                   ║
╚════════════════════════════════════════════════════════════╝

🚀 Initializing VSP Agent...
   🧠 Loading AI brain with Qwen2.5-0.5B...
   
[First time: Downloads ~1GB model]
Downloading (…)okenizer_config.json: 100%|███████| 1.2k/1.2k
Downloading (…)l.safetensors: 100%|████████████| 494M/494M
...

✅ VSP Agent is ready!
   🤖 Device: GPU

✅ VSP Agent is ready to chat!

Commands: 'exit' to quit, 'github' to check GitHub stats

💬 You: Who are you?

🤖 VSP Agent: I am VSP Agent, an AI assistant that provides 
information about Vishnu Suresh Perumbavoor. He is a Software 
Engineer, Singer, and YouTuber...

💬 You: What technologies does he use?

🤖 VSP Agent: He works with React, Node.js, FastAPI, Express, 
MongoDB, Docker, OHIF, Cornerstone3D, VTKjs, and DICOM...

💬 You: exit

👋 Thanks for chatting with VSP Agent! Goodbye! 🚀
```

---

## ✅ Summary

**Best way to test without installation:**

```bash
python -m vspagent.cli
```

This gives you:
- ✅ Full CLI experience
- ✅ No installation needed
- ✅ Instant testing
- ✅ Tests latest code changes

**Perfect for development and testing!** 🚀

