# DAY 5: Conditionals & Grade Calculator

## 📌 Problem Overview

Today you will learn:
1. How to use `if`, `elif`, `else` statements
2. How to use comparison operators (`>=`, `<=`, `and`)
3. How to check multiple conditions
4. How to validate user input
5. How to create a Grade Calculator

### What is this program doing?
- Taking percentage as input from user
- Checking percentage range using if-elif-else
- Assigning grades based on percentage
- Handling invalid inputs (above 100)
- Showing "Fail" for below 50%

---

## 📊 Grade System

| Percentage | Grade |
|------------|-------|
| 90 - 100 | A Grade |
| 80 - 89 | B Grade |
| 70 - 79 | C Grade |
| 60 - 69 | D Grade |
| 50 - 59 | E Grade |
| Below 50 | Fail |

---

## ❌ Common Errors & Solutions

### Error 1: Using str() instead of int()
```python
# WRONG ❌
percentage = str(input("Enter Percentage:"))  # Returns string

# RIGHT ✅
percentage = int(input("Enter Percentage:"))  # Returns integer
```
### Error 2: Missing indentation
```py
# WRONG ❌
if(percentage >= 90):
print("A Grade")  # IndentationError

# RIGHT ✅
if(percentage >= 90):
    print("A Grade")  # 4 spaces or tab
```
### Error 3: Typo in elif
```py
# WRONG ❌
elaf(percentage >=70):  # 'elaf' is wrong

# RIGHT ✅
elif(percentage >=70):  # 'elif' is correct
```
### Error 4: Using semicolon instead of colon
```py
# WRONG ❌
elif(percentage >=70 and percentage <=79);  # semicolon ❌

# RIGHT ✅
elif(percentage >=70 and percentage <=79):  # colon ✅
```
### Error 5: Typo in variable name

```py 
# WRONG ❌
elif(percentage >= 60 and percentege <=69):  # 'percentege' typo

# RIGHT ✅
elif(percentage >= 60 and percentage <=69):  # 'percentage' correct
```

### Error 6: Missing colon after else
```py
# WRONG ❌
else  # Missing colon

# RIGHT ✅
else:  # Colon required
```
## 📚 Resources to Learn (English)
### 1. W3Schools (Best for beginners)

Topic	Link
- If Else:	https://www.w3schools.com/python/python_conditions.asp
- Comparison Operators:	https://www.w3schools.com/python/python_operators_comparison.asp
- Logical Operators:	https://www.w3schools.com/python/python_operators_logical.asp

### 2. Programiz (Simple explanations)

Topic	Link
- If-Else Statement:	https://www.programiz.com/python-programming/if-elif-else
- Operators:	https://www.programiz.com/python-programming/operators

### 3. GeeksforGeeks (Detailed)


Topic	Link
- Conditional Statements:	https://www.geeksforgeeks.org/python-if-else/
- Nested If:	https://www.geeksforgeeks.org/nested-if-statement-in-python/

### 4. YouTube Videos (Hindi/English)

Channel	Link	
- CodeWithHarry:	https://youtu.be/7wnove7K-ZQ?t=2000	
- Apna College:	https://youtu.be/med2BtChVMA?t=300
- freeCodeCamp:	https://youtu.be/rfscVS0vtbw?t=3000	

### 5. Python Official Docs
- If Statement:	https://docs.python.org/3/tutorial/controlflow.html#if-statements