# DAY 17: Modules & Packages - Custom Package

## What You Will Learn
- How to create your own Python package
- What is `__init__.py` and why we need it
- How to import from custom packages
- How to organize code in multiple files

## Why Make a Package?
- Organize code in multiple files
- Reuse code across different projects
- Share your code with others
- Keep code clean and maintainable

## Folder Structure You Need to Create
```
day-17-modules/
│
├── main.py
│
└── MHAKModule/
├── init.py
├── basic.py
└── advance.py"

```
## Step 1: Create the Package Folder
Create a folder named `MHAKModule` (any name works)

## Step 2: Create `__init__.py` inside the folder
This file makes the folder a Python package.

```python
# File: MHAKModule/__init__.py

from .basic import add, sub, mul, div
from .advance import square, cube, power, factorial

__version__ = "1.0.0"
__author__ = "Hamid" #You can write your name instead of this
```
## Step 3: Create basic.py inside the folder
```py
# File: MHAKModule/basic.py

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b
```

## Step 4: Create advance.py inside the folder
```py
# File: MHAKModule/advance.py

import math

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def power(x, y):
    return x ** y

def factorial(n):
    return math.factorial(n)

def sqrt(n):
    return math.sqrt(n)
```
## Step 5: Create main.py to use the package
```py
# File: main.py

from MHAKModule.basic import add, sub, mul, div
from MHAKModule.advance import square, cube

print("=" * 40)
print("CUSTOM PACKAGE DEMO".center(40))
print("=" * 40)

print(f"\n10 + 5 = {add(10, 5)}")
print(f"10 - 5 = {sub(10, 5)}")
print(f"10 x 5 = {mul(10, 5)}")
print(f"10 / 5 = {div(10, 5)}")
print(f"Square of 5 = {square(5)}")
print(f"Cube of 5 = {cube(5)}")

print("\n" + "=" * 40)
print("PACKAGE WORKING!".center(40))
print("=" * 40)
```
## How to Run
Open terminal and run:
```
cd day-17-modules
python main.py
```
## Expected output:
```
========================================
        CUSTOM PACKAGE DEMO
========================================

10 + 5 = 15
10 - 5 = 5
10 x 5 = 50
10 / 5 = 2.0
Square of 5 = 25
Cube of 5 = 125

========================================
         PACKAGE WORKING!
========================================
```

## Common Errors and Solutions
- **Error:** ModuleNotFoundError: No module named 'MHAKModule'

- **Solution:** Make sure you have __init__.py file inside the MHAKModule folder

- **Error:** ImportError: cannot import name 'add'

- **Solution:** Check spelling of function names in both files

- **Error:** Running from wrong directory

- **Solution:** Use cd command to go into the folder that contains MHAKModule folder


## 🌟 What You Achieved Today

| Before Today | After Today |
|--------------|-------------|
| Only one file | Multiple organized files |
| Couldn't make packages | Can create own packages |
| Confused about imports | Understand import system |
| Beginner | Package Creator! |

## 📈 Your Progress
- Day 1 🌱 █░░░░░░░░░ Started
- Day 5 🌿 ███░░░░░░░ Getting there
- Day 10 🌳 ██████░░░░ Halfway done
- Day 15 🚀 ████████░░ Almost there
- Day 17 ⭐ █████████░ Package Master!
- Day 30 🏆 ██████████ Full Python Pro!


---

**🎊 KEEP CODING! SEE YOU ON DAY 18! 🎊**