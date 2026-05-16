# DAY 1: Python Basics - Print, Variables & f-strings

## 📌 Problem Overview

Today you will learn:
1. How to use `print()` function
2. How to create variables (`name = "Hamid"`)
3. How to use `f-strings` for formatting
4. How to create ASCII art and bio printer

### What is this program doing?
- Printing a bio/profile card
- Using normal `print()` with commas
- Using `f-strings` (better way to print variables)

---

## ❌ Common Errors & Solutions

### Error 1: Missing closing bracket
```python
# WRONG ❌
print("Hello World

# RIGHT ✅
print("Hello World")
```
### Error 2: Missing quotes
```python
# WRONG ❌
name = Hamid

# RIGHT ✅
name = "Hamid"
```
### Error 3: Variable not defined
```python
# WRONG ❌
print(my_name)  # my_name never created

# RIGHT ✅
my_name = "Hamid"
print(my_name)
```
### Error 4: Wrong case in variable name
```python
# WRONG ❌
Name = "Hamid"
print(name)  # 'name' is different from 'Name'

# RIGHT ✅
Name = "Hamid"
print(Name)  # Use same case
```
### Error 5: f-string missing 'f'
```python
# WRONG ❌
print("My name is {name}")  # Will print {name} as text

# RIGHT ✅
print(f"My name is {name}")  # f is must before quotes
```

# 📚 Resources to Learn (English)
## 1 W3Schools (Best for beginners)
Topic	Link
- Python Print	https://www.w3schools.com/python/ref_func_print.asp
- Python Variables	https://www.w3schools.com/python/python_variables.asp
Python Strings	https://www.w3schools.com/python/python_strings.asp
- f-strings	https://www.w3schools.com/python/ref_string_format.asp

## 2. Programiz (Simple explanations)
Topic	Link

- Print function: https://www.programiz.com/python-programming/methods/built-in/print
- Variables:	https://www.programiz.com/python-programming/variables-constants-literals

## 3. GeeksforGeeks (Detailed)

Topic Link

- Python Basics: https://www.geeksforgeeks.org/python-programming-language/learn-python-tutorial/

## 4. YouTube Videos (Hindi/English)

Channel	Link 

- CodewithHarry: https://youtu.be/7wnove7K-ZQ?si=g1cAPRRoLUvxJODj
- freeCodeCamp: https://youtu.be/rfscVS0vtbw

## 5. Python Official Docs
Topic	Link

- Print function: https://docs.python.org/3/library/functions.html#print
- f-strings: https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals
