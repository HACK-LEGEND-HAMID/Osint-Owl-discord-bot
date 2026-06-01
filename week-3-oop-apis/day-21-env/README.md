# DAY 21: Environment Variables - Secure App

## 📌 Problem Overview

Today you will learn:
1. What are Environment Variables
2. Why we need them for security
3. How to use `python-dotenv` module
4. How to keep API keys and passwords safe
5. How to create `.env` file and `.gitignore`

### What are Environment Variables?
- Variables that live outside your code
- Store sensitive data like passwords, API keys
- Different for each computer (not shared on GitHub)

---

## ❌ What Happens If You DON'T Use Environment Variables?

### Scenario 1: Hacker Finds Your Code on GitHub
```python
# Your code on GitHub (WRONG ❌)
API_KEY = "sk-1234567890abcdef"
PASSWORD = "mysecretpass123"
DB_URL = "postgres://admin:password@database.com"
```
## Hacker can:
- Steal your API key and use your paid services

- Hack your database and delete all data

- Access user passwords and personal info

- Sell your API key on dark web

- Run up thousands of dollars in charges on your account

## Scenario 2: Your Friend Sees Your Screen
```py
# You showing code to friend (WRONG ❌)
TOKEN = "ODQyMTIzNDU2Nzg5MDEyMzQ1.GhIJKLMNOPQRSTUVWXYZ"
```
### Friend can:
- Take your Discord bot token

- Run their own bot with your identity

- Spam users and get YOUR bot banned

- Delete all your servers

## Scenario 3: You Share Code for Help
```py 
# You paste code on Stack Overflow (WRONG ❌)
EMAIL_PASSWORD = "mypassword123"
DATABASE_PASSWORD = "admin123"
```
### Anyone on internet can:

- Access your email account

- Send spam from your email

- Reset your passwords

- Steal your identity

## ✅ With Environment Variables (SECURE)
```py
# Your code on GitHub (SAFE ✅)
import os
API_KEY = os.getenv("API_KEY")  # Reads from .env file
PASSWORD = os.getenv("PASSWORD")
```

- **Hacker sees:** Nothing! Just os.getenv()
- **Your secrets stay:** On your computer only

## 📚 Two Ways to Use Environment Variables
Way 1: Direct from System (No extra install)
```python
import os

# Set in terminal first (Windows)
# set API_KEY=abc123

# Set in terminal first (Mac/Linux)
# export API_KEY=abc123

API_KEY = os.environ.get("API_KEY")
print(API_KEY)
```
Way 2: Using python-dotenv (Best Practice)
```bash
# First install
pip install python-dotenv
python
import os
from dotenv import load_dotenv

load_dotenv()  # Loads .env file

API_KEY = os.getenv("API_KEY")
PASSWORD = os.getenv("PASSWORD")
```

## 📚 Resources
Topic	Link
- python-dotenv:	https://pypi.org/project/python-dotenv/
- Environment Variables:	https://www.w3schools.com/python/python_variables.asp