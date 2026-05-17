# DAY 2: Variables & Age Calculator

## 📌 Problem Overview

Today you will learn:
1. How to take user input using `input()` function
2. How to convert string to integer using `int()`
3. How to perform mathematical operations with variables
4. How to create an Age Calculator

### What is this program doing?
- Taking birth year and current year as input from user
- Converting string input to integer numbers
- Calculating age using formula: `age = current_year - birth_year`
- Displaying the result in a formatted way

---

## ❌ Common Errors & Solutions

### Error 1: Cannot convert string to int
```python
# WRONG ❌
birth_year = input("Enter birth year: ")  # Returns string like "2005"
age = 2025 - birth_year  # ERROR! Can't subtract string from number

# RIGHT ✅
birth_year = int(input("Enter birth year: "))  # Converts to integer 2005
age = 2025 - birth_year  # Works fine!
```
### Error 2: Forgot to convert one of the inputs
```python
# WRONG ❌
birth_year = int(input("Enter birth year: "))
current_year = input("Enter current year: ")  # Missing int()
age = current_year - birth_year  # ERROR! current_year is string

# RIGHT ✅
birth_year = int(input("Enter birth year: "))
current_year = int(input("Enter current year: "))
age = current_year - birth_year
```

### Error 3: Using wrong variable name
```python
# WRONG ❌
birth_year = int(input("Enter birth year: "))
current_year = int(input("Enter current year: "))
my_age = current_year - birth_year  # Variable name 'my_age'
print(age)  # ERROR! 'age' is not defined

# RIGHT ✅
birth_year = int(input("Enter birth year: "))
current_year = int(input("Enter current year: "))
age = current_year - birth_year
print(age)  # Works fine!
```

### Error 4: Missing closing bracket or parenthesis
```python
# WRONG ❌
birth_year = int(input("Enter birth year: ")  # Missing closing )

# RIGHT ✅
birth_year = int(input("Enter birth year: "))
```

## 📚 Resources to Learn (English)
### 1. W3Schools (Best for beginners)

Topic	Link

- User Input: https://www.w3schools.com/python/python_user_input.asp
- Type Conversion: https://www.w3schools.com/python/python_casting.asp
- Variables: https://www.w3schools.com/python/python_variables.asp
- Numbers :https://www.w3schools.com/python/python_numbers.asp

### 2. Programiz (Simple explanations)

Topic	Link

- Input/Output: https://www.programiz.com/python-programming/input-output-import
- Type Conversion: https://www.programiz.com/python-programming/type-conversion

### 3. GeeksforGeeks (Detailed)

Topic	Link

- Taking Input:	https://www.geeksforgeeks.org/taking-input-in-python/
- Type Casting:	https://www.geeksforgeeks.org/type-casting-in-python/

### 4. YouTube Videos (Hindi/English)

- CodeWithHarry:	https://youtu.be/7wnove7K-ZQ?t=500
- Apna College:	https://youtu.be/med2BtChVMA
- freeCodeCamp:	https://youtu.be/rfscVS0vtbw?t=1200	

### 5. Python Official Docs

- Input Function:	https://docs.python.org/3/library/functions.html#input
- int() Function:	https://docs.python.org/3/library/functions.html#int

