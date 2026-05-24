# DAY 8: Functions - Calculator

## 📌 Problem Overview

Today you will learn:
1. How to define functions using `def`
2. How to pass parameters to functions
3. How to return values from functions
4. How to use `if-elif` inside functions
5. How to import and use `math` module

### What is this program doing?
- Displaying menu with 8 calculator functions
- Taking user choice as input
- Calling appropriate function based on choice
- Basic calculator: add, subtract, multiply, divide, power
- Intermediate calculator: square root, factorial, absolute value

---

## 📚 Functions Cheatsheet

```python
# 1. BASIC FUNCTION (no parameters, no return)
def say_hello():
    print("Hello!")

# 2. FUNCTION WITH PARAMETERS
def add(a, b):
    return a + b

# 3. FUNCTION WITH RETURN VALUE
def square(x):
    return x * x

# 4. FUNCTION WITH MULTIPLE RETURNS
def get_operations(a, b):
    return a+b, a-b, a*b

# 5. FUNCTION WITH DEFAULT PARAMETER
def greet(name="Guest"):
    print(f"Hello {name}")

# 6. CALLING FUNCTIONS
result = add(5, 3)     # result = 8
greet("Hamid")          # Hello Hamid
greet()    
```
## 🧮 Math Module Functions

| Function | What it does | Example | Output |
|----------|--------------|---------|--------|
| `math.sqrt(x)` | Square root | `math.sqrt(25)` | `5.0` |
| `math.factorial(x)` | Factorial | `math.factorial(5)` | `120` |
| `math.fabs(x)` | Absolute value | `math.fabs(-10)` | `10.0` |
| `math.pow(x,y)` | Power | `math.pow(2,3)` | `8.0` |
| `math.pi` | Pi value | `math.pi` | `3.14159` |
| `math.ceil(x)` | Round up | `math.ceil(4.2)` | `5` |
| `math.floor(x)` | Round down | `math.floor(4.9)` | `4` |
| `math.sin(x)` | Sine value | `math.sin(90)` | `0.8939` |
| `math.cos(x)` | Cosine value | `math.cos(0)` | `1.0` |
| `math.log(x)` | Natural log | `math.log(10)` | `2.3025` |
| `math.exp(x)` | e^x | `math.exp(1)` | `2.7182` |             # Hello Guest

## ❌ Common Errors & Solutions
### Error 1: String vs Integer comparison
```py 
# WRONG ❌
function = input("Enter choice: ")  # Returns "1" (string)
if function == 1:  # Comparing string with integer

# RIGHT ✅
function = input("Enter choice: ")  # "1" (string)
if function == "1":  # Compare string with string

```
### Error 2: Division by zero
```py 
# WRONG ❌
def basic_cal(a,b,choice):
    if choice == '3':
        return a / b  # If b is 0, ZeroDivisionError

# RIGHT ✅
def basic_cal(a,b,choice):
    if choice == '3':
        if b == 0:
            return "Error: Cannot divide by zero"
        return a / b
```

### Error 3: Function not returning value

```py 
# WRONG ❌
def add(a,b):
    result = a + b  # No return statement

# RIGHT ✅
def add(a,b):
    return a + b  # Return the result
```
### Error 4: Wrong parameter order
```py
# WRONG ❌
def basic_cal(a,b,choice):  # Parameters: a, b, choice
    return a + b

# Calling with wrong order
result = basic_cal("1", 5, 3)  # Wrong order!

# RIGHT ✅
result = basic_cal(5, 3, "1")  # Correct order
```

### Error 5: Missing import
```py
# WRONG ❌
result = math.sqrt(25)  # NameError: math not imported

# RIGHT ✅
import math
result = math.sqrt(25)
```
### Error 6: Typo in variable name

```py 
# WRONG ❌
print("5-Squre")  # Typo: "Squre"
print("5-Square")  # Correct spelling

# WRONG ❌
print("6-Squre Root")  # Typo
print("6-Square Root")  # Correct
```
## 📚 Resources to Learn (English)
### 1. W3Schools

Topic	Link
- Functions:	https://www.w3schools.com/python/python_functions.asp
- Math Module:	https://www.w3schools.com/python/module_math.asp
- Return Values:	https://www.w3schools.com/python/gloss_python_function_return_value.asp
### 2. Programiz
Topic	Link
- Python Functions:	https://www.programiz.com/python-programming/function
- Math Module:	https://www.programiz.com/python-programming/modules/math
### 3. GeeksforGeeks
Topic	Link
- Functions:	https://www.geeksforgeeks.org/python-functions/
- Math Module:	https://www.geeksforgeeks.org/python-math-module/
### 4. YouTube Videos
Channel	Link
- CodeWithHarry:	https://youtu.be/7wnove7K-ZQ?t=3500	
- Apna College:	https://youtu.be/med2BtChVMA?t=1800	Math Module
- freeCodeCamp:	https://youtu.be/rfscVS0vtbw?t=6000	
### 5. Python Official Docs
Topic	Link
- Functions:	https://docs.python.org/3/tutorial/controlflow.html#defining-functions
- Math Module:	https://docs.python.org/3/library/math.html