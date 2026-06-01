# DAY 18: Virtual Environment & GitHub Setup

## What is Virtual Environment?
Isolated space for each Python project. Different projects can have different package versions without conflict.

## Why Need It?
- Each Discord bot can have different package versions
- No conflicts between projects
- Clean main Python installation

## Step by Step Setup

### 1. Create Virtual Environment
```bash
python -m venv venv
```
# 2. Activate It

## Windows
```bash
venv\Scripts\activate
```
## Mac/Linux
```bash
source venv/bin/activate
```
# 3. Install Packages
```bash
pip install discord.py python-dotenv
```
# 4. Save Requirements
```bash
pip freeze > requirements.txt
```
# 5. Deactivate
```bash
deactivate
```
## What Files to Upload on GitHub?
✅ Upload These:
- text
- bot.py
- requirements.txt
- .env.example
- .gitignore
- README.md
## ❌ Do NOT Upload

- venv/           (too big, machine specific)
- .env            (contains secret bot token)
- __pycache__/    (Python cache)
- .gitignore File (Create This)
- gitignore
## Virtual Environment (NEVER upload)
```bash
venv/
env/
```
## Secrets (NEVER upload)
```bash
.env
.env.local
token.txt
```
## Python cache
```bash
__pycache__/
*.pyc
```
## IDE settings
```bash
.vscode/
.idea/
```
## OS files
```bash
.DS_Store
Thumbs.db
.env File (SECRET - Don't Share)
```

## File: .env
## ⚠️ NEVER upload this to GitHub!
```bash
DISCORD_BOT_TOKEN=your_real_token_here
BOT_PREFIX=!
.env.example File (SHARE This)
```
## File: .env.example
## ✅ You CAN share this
```bash
DISCORD_BOT_TOKEN=your_bot_token_here
BOT_PREFIX=!
```
# Bot Code Example
```python
# bot.py
import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_BOT_TOKEN')

bot =commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user} is online!')

bot.run(TOKEN)
```
# GitHub Push Steps
```bash
# 1. Initialize git
git init

# 2. Check what will be uploaded
git status

# 3. Add files
git add .

# 4. Commit
git commit -m "First commit"

# 5. Connect to GitHub
git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git

# 6. Push
git push -u origin main

```
# How Others Use Your Bot
```bash
# 1. Clone
git clone YOUR_REPO_URL
cd REPO_NAME

# 2. Create virtual environment
python -m venv venv

# 3. Activate
venv\Scripts\activate

# 4. Install packages
pip install -r requirements.txt

# 5. Create .env file with their own token

# 6. Run
python bot.py
```

# Why Hide Bot Token?
```
❌ Token on GitHub → Hackers steal → Bot gets banned
✅ Token in .env → Hidden from GitHub → Bot stays safe
```

## Quick Checklist
- Created virtual environment

- Activated it

- Installed packages

- Created requirements.txt

- Created .gitignore

- Added venv/ to .gitignore

- Added .env to .gitignore

- Created .env (local, secret)

- Created .env.example (for sharing)

- Checked git status (no secrets showing)

- Pushed to GitHub