# DAY 13: Error Handling - Calculator with Try-Except

## 📌 Problem Overview

Today you will learn:
1. How to use `try-except` for error handling
2. Different types of errors (ValueError, ZeroDivisionError, etc.)
3. How to prevent program from crashing
4. How to show user-friendly error messages
5. How to use `else` and `finally` blocks

### What is this program doing?
- Calculator with full error handling
- Handles invalid user input (text instead of numbers)
- Handles division by zero
- Handles negative square root
- Handles negative factorial
- Graceful exit on Ctrl+C

---

## 📚 Error Handling Syntax

```python
# BASIC TRY-EXCEPT
try:
    # Code that might cause error
    num = int(input("Enter number: "))
except ValueError:
    # Runs if ValueError occurs
    print("Invalid input!")

# MULTIPLE EXCEPTIONS
try:
    num = int(input("Enter number: "))
    result = 100 / num
except ValueError:
    print("Not a number!")
except ZeroDivisionError:
    print("Can't divide by zero!")

# TRY-EXCEPT-ELSE-FINALLY
try:
    num = int(input("Enter number: "))
except ValueError:
    print("Error!")
else:
    print("No error occurred!")
finally:
    print("This always runs!")
```


## ❌ Common Errors & Solutions
### Error 1: Comparing string with integer
```python
# WRONG ❌
if choice == 1:  # '1' is string, 1 is integer

# RIGHT ✅
if choice == '1':  # Compare string with string
```
### Error 2: Wrong variable name
```python
# WRONG ❌
funtion = input("Enter choice: ")  # 'funtion' typo

# RIGHT ✅
function = input("Enter choice: ")  # 'function' correct
```
### Error 3: Missing parentheses
```python
# WRONG ❌
if function_lower() == 'q':  # 'function_lower' not defined

# RIGHT ✅
if function.lower() == 'q':  # .lower() method
```
### Error 4: Wrong variable in print
```python
# WRONG ❌
except Exception as f:
    print(f"Something went wrong: {e}")  # 'e' not defined

# RIGHT ✅
except Exception as e:
    print(f"Something went wrong: {e}")  # 'e' is correct
```
### Error 5: Typo in except keyword
```python
# WRONG ❌
accept ValueError:  # 'accept' is wrong

# RIGHT ✅
except ValueError:  # 'except' is correct
```
### Error 6: Wrong function name
```python
# WRONG ❌
result = intr_cal(num, function)  # 'intr_cal' typo

# RIGHT ✅
result = inter_cal(num, function)  # 'inter_cal' correct
```
### Error 7: Subtraction order wrong
```python
# WRONG ❌
elif choice == '2':
    return b - a  # Should be a - b

# RIGHT ✅
elif choice == '2':
    return a - b  # Correct order
```
### Error 8: Division condition wrong
```python
# WRONG ❌
if b == 1:  # Should check for 0, not 1

# RIGHT ✅
if b == 0:  # Check for zero
```

## 📚 Resources to Learn (English)
### 1. W3Schools
Topic	Link
- Try Except:	https://www.w3schools.com/python/python_try_except.asp
- Error Types:	https://www.w3schools.com/python/gloss_python_error_types.asp
- Finally Block:	https://www.w3schools.com/python/gloss_python_try_finally.asp
### 2. Programiz
Topic	Link
- Exception Handling:	https://www.programiz.com/python-programming/exception-handling
- Try Except Else:	https://www.programiz.com/python-programming/exception-handling/try-except-else
### 3. GeeksforGeeks
Topic	Link
- Errors and Exceptions:	https://www.geeksforgeeks.org/errors-and-exceptions-in-python/
- Multiple Exceptions:	https://www.geeksforgeeks.org/catch-multiple-exceptions-in-python/
### 4. YouTube Videos
Channel	Link
- CodeWithHarry:	https://youtu.be/7wnove7K-ZQ?t=6000	
- Apna College:	https://youtu.be/med2BtChVMA?t=3300
- freeCodeCamp:	https://youtu.be/rfscVS0vtbw?t=11000
### 5. Python Official Docs
Topic	Link
- Errors:	https://docs.python.org/3/tutorial/errors.html
- Built-in Exceptions:	https://docs.python.org/3/library/exceptions.html