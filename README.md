# 🤖 VSP Agent

[![PyPI version](https://badge.fury.io/py/vspagent.svg)](https://pypi.org/project/vspagent/)
[![Python Versions](https://img.shields.io/pypi/pyversions/vspagent.svg)](https://pypi.org/project/vspagent/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**AI-powered agent with information about Vishnu Suresh Perumbavoor. Powered by Qwen2.5-0.5B.**

## 🚀 Features

- 🧠 **AI Chat**: Interactive conversations powered by Qwen2.5-0.5B language model
- 📊 **GitHub Integration**: Check real-time GitHub statistics and repositories
- 💼 **Job Search**: Search LinkedIn jobs by role and location
- 📝 **Cover Letter Generator**: Automatically generate professional cover letters
- 🎯 **CLI Interface**: Easy-to-use command-line interface
- 🐍 **Python API**: Programmatic access to all features

## 📦 Installation

```bash
pip install vspagent
```

## 🎯 Quick Start

### CLI Mode

Simply run:

```bash
vspagent-py
```

This launches an **interactive chat session** with the VSP Agent!

**Example Chat Session:**
```
💬 You: Who is VSP?
🤖 VSP Agent: VSP stands for Vishnu Suresh Perumbavoor. He is the founder 
of VSP Enterprises and VSP Intelligence. He's a Software Engineer, Singer, 
and YouTuber...

💬 You: What technologies does he use?
🤖 VSP Agent: He works with React, Node.js, FastAPI, Docker, MongoDB...

💬 You: github
📊 GitHub Stats: 30 repos, 45 stars

💬 You: exit
👋 Thanks for chatting!
```

**Features:**
- 🤖 AI-powered conversations with Qwen2.5-0.5B
- 💬 Natural language understanding
- 🧠 Conversation memory (maintains context)
- ⚡ GPU acceleration (30-50x faster if available)
- 🔍 Special commands: `github`, `exit`

**Note:** Command is `vspagent-py` (not `vspagent`) to avoid conflicts with the JavaScript version.

### Python API

```python
from vspagent import VSPAgent, biodata

# Create agent instance
agent = VSPAgent()

# Initialize AI model
agent.init_ai()

# Chat with the agent
response = agent.chat("Who is VSP?")
print(response)

# Check GitHub stats
stats = agent.check_github()
print(f"Total Repos: {stats['total_repos']}")
print(f"Total Stars: {stats['total_stars']}")

# Search for jobs
jobs = agent.search_jobs("AI Engineer", "Kerala")
print(jobs['search_url'])

# Generate cover letter
letter = agent.generate_cover_letter("AI Engineer", "Google")
print(letter)

# Access biodata directly
print(biodata['creator'])
print(biodata['technologies'])
```

## 📚 API Reference

### `VSPAgent` Class

#### Methods

- **`init_ai()`**: Initialize the Qwen2.5-0.5B AI model
- **`chat(message, conversation_history=None)`**: Chat with the AI agent
- **`check_github(username="vishnusureshperumbavoor")`**: Get GitHub statistics
- **`search_jobs(role, location)`**: Search LinkedIn jobs
- **`generate_cover_letter(job_title, company)`**: Generate a cover letter

### `biodata` Dictionary

Contains comprehensive information about Vishnu Suresh Perumbavoor:
- Personal information
- Founder companies
- Technologies and skills
- Accomplishments
- Social media links

## 🛠️ Requirements

- Python 3.8+
- transformers >= 4.30.0
- torch >= 2.0.0
- requests >= 2.31.0

## 🎨 CLI Commands

When running in CLI mode:
- Type your message to chat with the agent
- Type `github` to check GitHub statistics
- Type `exit` or `quit` to exit

## 👨‍💻 About VSP

**Vishnu Suresh Perumbavoor** is the founder of VSP Enterprises and VSP Intelligence. He's a:
- Software Engineer
- Singer
- YouTuber
- Technology enthusiast

### 🏆 Accomplishments
- Won 3rd prize in Vaiga Agrihack 2023
- Participated in Rajasthan IT Hackathon 2023
- Won 1st prize in startup idea presentation at Palakkad

### 🔧 Technologies
React, Node.js, FastAPI, Express, MongoDB, Docker, OHIF, Cornerstone3D, VTKjs, DICOM

## 🔗 Connect

- 💼 [LinkedIn](https://www.linkedin.com/in/vishnu-suresh-perumbavoor/)
- 🐙 [GitHub](https://github.com/vishnusureshperumbavoor)
- 🐦 [Twitter](https://twitter.com/vspeeeeee)
- 📺 [YouTube](https://www.youtube.com/@vishnusureshperumbavoor9721/videos)
- 📷 [Instagram](https://www.instagram.com/vishnusureshperumbavoor/)

## 📄 License

MIT License - see LICENSE file for details

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 🐛 Issues

Found a bug? [Report it here](https://github.com/vishnusureshperumbavoor/vsp_bot/issues)

## 📈 Version

Current version: **2.2.0**

---

Made with ❤️ by Vishnu Suresh Perumbavoor

