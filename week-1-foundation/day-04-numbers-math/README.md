# DAY 4: Random Numbers & Dice Roller

## 📌 Problem Overview

Today you will learn:
1. How to use `random.randint()` function
2. How to create and use dictionaries `{}`
3. How to use multi-line strings (`""" """`)
4. How to create ASCII art dice faces
5. How to use `input()` as a pause mechanism

### What is this program doing?
- Waiting for user to press ENTER
- Generating random number between 1 and 6
- Displaying ASCII art of dice face
- Showing the rolled number

---

## ❌ Common Errors & Solutions

### Error 1: Missing colon in dictionary
```python
# WRONG ❌
1 """
┌─────────┐
│         │
└─────────┘"""

# RIGHT ✅
1: """
┌─────────┐
│         │
└─────────┘"""
```
### Error 2: Typo in function name
```py
# WRONG ❌
print("DICE ROLLER".cente(40))  # 'cente' is wrong

# RIGHT ✅
print("DICE ROLLER".center(40))  # 'center' is correct
```

### Error 3: Missing * operator
```py
# WRONG ❌
print("="40)  # TypeError

# RIGHT ✅
print("=" * 40)  # Multiply string
```
### Error 4: Wrong print function
```py
# WRONG ❌
printf(dice_faces[dice])  # 'printf' doesn't exist in Python

# RIGHT ✅
print(dice_faces[dice])  # 'print' is correct
```
### Error 5: Wrong f-string syntax
```py # WRONG ❌
print(f"You rolled: [dice]")  # Using [ ] instead of { }

# RIGHT ✅
print(f"You rolled: {dice}")  # Use { } for variables
```
### Error 6: Missing import
```py
# WRONG ❌
dice = random.randint(1, 6)  # NameError: random not imported

# RIGHT ✅
import random  # Must import first
dice = random.randint(1, 6)
```
## 📚 Resources to Learn (English)

### 1. W3Schools (Best for beginners)

Topic	Link
- Random Module:	https://www.w3schools.com/python/module_random.asp
- Dictionaries:	https://www.w3schools.com/python/python_dictionaries.asp
- randint():	https://www.w3schools.com/python/ref_random_randint.asp

### 2. Programiz (Simple explanations)
Topic	Link

- Random Numbers	https://www.programiz.com/python-programming/modules/random
- Dictionary	https://www.programiz.com/python-programming/dictionary

### 3. GeeksforGeeks (Detailed)

Topic	Link
- random.randint()	https://www.geeksforgeeks.org/python-randint-function/
- Dictionary Methods	https://www.geeksforgeeks.org/python-dictionary/

### 4. YouTube Videos (Hindi/English)

Channel	Link	
- CodeWithHarry:	https://youtu.be/7wnove7K-ZQ?t=1500	
- Apna College:	https://youtu.be/med2BtChVMA?t=900
- freeCodeCamp	https://youtu.be/rfscVS0vtbw?t=2500	

### 5. Python Official Docs

Topic	Link
- random module	https://docs.python.org/3/library/random.html
- Dictionary	https://docs.python.org/3/tutorial/datastructures.html#dictionaries

