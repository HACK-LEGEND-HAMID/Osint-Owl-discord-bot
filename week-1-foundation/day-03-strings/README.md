# DAY 3: String Methods & Text Formatter

## 📌 Problem Overview

Today you will learn:
1. String methods (`upper()`, `lower()`, `title()`, etc.)
2. String formatting (`center()`, `ljust()`, `rjust()`)
3. Text wrapping using `textwrap` module
4. String slicing (`[::-1]` for reverse)
5. Word and character counting

### What is this program doing?
- Taking user input as text
- Applying different string formatting methods
- Showing uppercase, lowercase, title case versions
- Aligning text (left, right, center)
- Counting words and characters
- Reversing the text

---

## ❌ Common Errors & Solutions

### Error 1: Missing * operator
```python
# WRONG ❌
print("="50)  # TypeError: 'str' and 'int'

# RIGHT ✅
print("=" * 50)  # Multiply string by number
```
### Error 2: Missing + operator
```python
# WRONG ❌
print("\n" "="*50)  # Works but not clear

# RIGHT ✅
print("\n" + "="*50)  # Clear concatenation
```
### Error 3: Missing dot (.) for method call
```python
# WRONG ❌
print("ALL FORMATS"center(50))  # SyntaxError

# RIGHT ✅
print("ALL FORMATS".center(50))  # String method call
```

### Error 4: Wrong variable name
```python
# WRONG ❌
print(txt.upper())  # 'txt' not defined

# RIGHT ✅
print(text.upper())  # Variable name is 'text'
```
### Error 5: Indentation error
```python
# WRONG ❌
   print(text.capitalize())  # Extra space at start

# RIGHT ✅
print(text.capitalize())  # No extra space
```
### Error 6: Missing closing bracket
```py
# WRONG ❌
print(text.rjust(70)  # Missing closing )

# RIGHT ✅
print(text.rjust(70))
```
### Error 7: Wrong slicing for reverse
```py
# WRONG ❌
print(text[:-1])  # Removes last character only

# RIGHT ✅
print(text[::-1])  # Full string reverse
```

### Error 8: Wrong function name
```py
# WRONG ❌
print(f"Total Words: {le(words)}")  # 'le' not defined

# RIGHT ✅
print(f"Total Words: {len(words)}")  # 'len' function
```
### Error 9: Missing import
```py
# WRONG ❌
print(textwrap.fill(text, width=50))  # NameError: textwrap not imported

# RIGHT ✅
import textwrap  # Must import first
```
## 📚 Resources to Learn (English)
### 1. W3Schools (Best for beginners)

Topic	Link
- String Methods:	https://www.w3schools.com/python/python_strings_methods.asp
- String Formatting:	https://www.w3schools.com/python/python_string_formatting.asp
- String Slicing:	https://www.w3schools.com/python/python_string_slicing.asp

### 2. Programiz (Simple explanations)

Topic	Link
- String Methods:	https://www.programiz.com/python-programming/string
- String Operations:	https://www.programiz.com/python-programming/string-methods

### 3. GeeksforGeeks (Detailed)

Topic	Link

- String Methods: https://www.geeksforgeeks.org/python-string-methods/
- textwrap module:	https://www.geeksforgeeks.org/textwrap-module-in-python/

### 4. YouTube Videos (Hindi/English)

Channel	Link

- CodeWithHarry: 	https://youtu.be/7wnove7K-ZQ?t=800
- Apna College:	https://youtu.be/med2BtChVMA?t=600	
- freeCodeCamp:	https://youtu.be/rfscVS0vtbw?t=1800

### 5. Python Official Docs

Topic	Link
- String Methods:	https://docs.python.org/3/library/stdtypes.html#string-methods
- textwrap:	https://docs.python.org/3/library/textwrap.html

