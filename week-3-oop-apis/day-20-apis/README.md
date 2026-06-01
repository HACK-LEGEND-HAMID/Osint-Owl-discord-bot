# DAY 20: APIs - Joke Fetcher

## 📌 Problem Overview

Today you will learn:
1. What is API (Application Programming Interface)
2. How to use `requests` module to fetch data from internet
3. How to parse JSON response from API
4. How to create a Joke Generator app

### What is API?
- API allows different applications to talk to each other
- You send a request → API returns data (usually in JSON format)
- Like ordering food: You order (request) → Waiter brings food (response)

---

## ❌ Common Errors & Solutions

### Error 1: Wrong module name
```python
# WRONG ❌
import request  # Missing 's'

# RIGHT ✅
import requests  # With 's'
```

### Error 2: Variable name case mismatch
```py
# WRONG ❌
Choice = input("Choose: ")  # Capital C
if choice == '1':           # Small c (different variable)

# RIGHT ✅
choice = input("Choose: ")  # Small c everywhere
```
### Error 3: Comparing string with integer
```py
# WRONG ❌
elif choice == 2:  # String vs integer

# RIGHT ✅
elif choice == '2':  # String vs string
```
### Error 4: Assignment instead of comparison
```py
# WRONG ❌
elif choice = '3':  # = is assignment, not comparison

# RIGHT ✅
elif choice == '3':  # == is comparison
```
### Error 5: Colon after break
```py
# WRONG ❌
break:  # No colon after break

# RIGHT ✅
break  # Just break
```
### Error 6: requests not installed

```py
# WRONG ❌
import requests  # ModuleNotFoundError

# RIGHT ✅
# First install: pip install requests
```
### Error 7: No internet connection
```py
# WRONG ❌
response = requests.get(url)  # May crash

# RIGHT ✅
try:
    response = requests.get(url)
except:
    print("No internet connection!")
```

## 📚 API Resources Used
API	URL	Use
- Official Joke API:	https://official-joke-api.appspot.com/random_jok
- JokeAPI:	https://v2.jokeapi.dev/joke/Programming	
- JokeAPI	https://v2.jokeapi.dev/joke/Dark	

## 📚 Resources to Learn
Topic	Link
- Python Requests:	https://www.w3schools.com/python/module_requests.asp
- JSON in Python:	https://www.w3schools.com/python/python_json.asp
- Free APIs:	https://github.com/public-apis/public-apis