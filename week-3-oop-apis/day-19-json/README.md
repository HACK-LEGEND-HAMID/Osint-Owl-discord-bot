# DAY 19: JSON Settings Manager

## What You Will Learn
- What is JSON and why use it
- How to save settings to JSON file
- How to load settings from JSON file
- How to create a settings manager for Discord bot

## What is JSON?
JSON = JavaScript Object Notation. It's a way to store data in readable text format.

## Why JSON for Settings?
- Human readable (easy to edit)
- Works with all programming languages
- Perfect for bot configuration files
- Persistent storage (saves between bot restarts)

## JSON Example
```json
{
    "username": "Hamid",
    "theme": "dark",
    "volume": 80
}
```
## JSON vs Dictionary
#### Python Dictionary	
```py
 {"name": "Hamid"}	
```
#### JSON File**
```py
{"name": "Hamid"}
```
#### Python Dictionary
```py
Lives in memory	
```
#### JSON File
```py
Saved on disk
```
#### Python Dictionary
```py
Lost when program ends
```
#### JSON File
```py
Saved forever
```
#### Python Dictionary
```py
Fast access	
```
#### JSON File
```py
Slower but permanent
```

## JSON Methods Reference

| Method | What it does |
|--------|--------------|
| `json.load(file)` | Read JSON file → Python dictionary |
| `json.dump(data, file)` | Save Python dictionary → JSON file |
| `json.loads(string)` | Convert JSON string → dictionary |
| `json.dumps(data)` | Convert dictionary → JSON string |

## JSON Parameters Explained
```python
# indent=4 makes it readable with 4 spaces
json.dump(settings, f, indent=4)

# Without indent (everything in one line)
json.dump(settings, f)

# sort_keys=True sorts alphabetically
json.dump(settings, f, indent=4, sort_keys=True)
```

## ❌ Common Errors & Solutions

### Error 1: Variable name mismatch
```python
# WRONG ❌
SETTING_FILE = "settings.json"  # Variable name
if os.path.exists(FILE):        # Using different name 'FILE'

# RIGHT ✅
FILE = "settings.json"          # Same name everywhere
```
### Error 2: Wrong variable in json.load()
```py
# WRONG ❌
settings = json.load(FILE)      # Should be file object, not string

# RIGHT ✅
settings = json.load(f)         # 'f' is file object
```
### Error 3: Missing * operator in print
```py
# WRONG ❌
print("="30)                    # Missing *

# RIGHT ✅
print("=" * 30)                 # With *
```
### Error 4: Wrong variable name in loop
```py
# WRONG ❌
print(f"  {setting}: {value}")  # 'setting' not defined

# RIGHT ✅
print(f"  {key}: {value}")      # 'key' is correct
```
### Error 5: Wrong case in variable
```py
# WRONG ❌
if Choice == '1':               # 'Choice' capital C

# RIGHT ✅
if choice == '1':               # 'choice' small c
```

### Error 6: Comparing string with integer
```py
# WRONG ❌
elif choice == 2:               # String vs integer

# RIGHT ✅
elif choice == '2':             # String vs string
```
### Error 7: Colon after break
```py
# WRONG ❌
break:                          # No colon after break

# RIGHT ✅
break                           # Just break
```
## 📈 Your Progress

- Day 1  🌱 █░░░░░░░░░  Started
- Day 5  🌿 ███░░░░░░░  Getting there
- Day 10 🌳 ██████░░░░  Halfway done
- Day 15 🚀 ████████░░  Almost there
- Day 17 ⭐ █████████░  Package Master!
- Day 19 💾 █████████░  JSON Settings Master!
- Day 30 🏆 ██████████  Full Python Pro!

## 📚 Resources
Topic	Link:
- **JSON in Python:**	https://www.w3schools.com/python/python_json.asp
- **json.dump():**	https://docs.python.org/3/library/json.html