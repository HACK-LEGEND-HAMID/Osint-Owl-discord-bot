# DAY 6: Lists & While Loops - To-Do List

## 📌 Problem Overview

Today you will learn:
1. How to create and use lists `[]`
2. How to use `while` loops for repeated input
3. How to use `append()` to add items to list
4. How to use `enumerate()` to loop through list with index
5. How to use `break` to exit a loop
6. How to use `lower()` for case-insensitive comparison

### What is this program doing?
- Creating an empty list to store tasks
- Using while loop to take multiple task inputs
- Breaking loop when user types 'done'
- Adding each task to the list using `append()`
- Displaying all tasks with numbers using `enumerate()`
- Showing "No Tasks Added" if list is empty

---

## ❌ Common Errors & Solutions

### Error 1: Missing dot in method call
```python
# WRONG ❌
print("TO-DO LIST".center40))  # Missing dot and parentheses issue

# RIGHT ✅
print("TO-DO LIST".center(40))  # .center(40) is correct
```

### Error 2: Wrong case in True keyword
```py
# WRONG ❌
while true:  # Python is case-sensitive, 'true' is not defined

# RIGHT ✅
while True:  # 'True' with capital T
```
### Error 3: Wrong variable name case

```py
# WRONG ❌
task = input(f"Task {Task_number}: ")  # 'Task_number' not defined

# RIGHT ✅
task = input(f"Task {task_number}: ")  # 'task_number' is correct
```

### Error 4: Wrong variable name (list name)
```py
# WRONG ❌
to_do_list = []  # declared as 'to_do_list'
todo_list.append(task)  # using 'todo_list' (missing underscore)

# RIGHT ✅
to_do_list = []  # declared as 'to_do_list'
to_do_list.append(task)  # use same name 'to_do_list'
```

### Error 5: Wrong f-string syntax
```py
# WRONG ❌
print(f"[i]. {task}")  # Prints literal "[i]" not the variable

# RIGHT ✅
print(f"{i}. {task}")  # 'i' is variable, no brackets around it
```
### Error 6: Missing colon after else
```py
# WRONG ❌
else  # Missing colon

# RIGHT ✅
else:  # Colon is required
```

### Error 7: Extra closing parenthesis
```py
# WRONG ❌
print("TO-DO LIST".center40))  # Two closing parentheses

# RIGHT ✅
print("TO-DO LIST".center(40))  # One closing parenthesis
```

## 📚 Resources to Learn (English)


### 1. W3Schools (Best for beginners)
Topic	Link
- Lists:	https://www.w3schools.com/python/python_lists.asp
- While Loops:	https://www.w3schools.com/python/python_while_loops.asp
- List Methods:	https://www.w3schools.com/python/python_lists_methods.asp
### 2. Programiz (Simple explanations)
Topic Link
- Python Lists:	https://www.programiz.com/python-programming/list
- While Loop: https://www.programiz.com/python-programming/while-loop
### 3. GeeksforGeeks (Detailed)
Topic	Link
- List in Python	https://www.geeksforgeeks.org/python-list/
- Enumerate	https://www.geeksforgeeks.org/enumerate-in-python/
### 4. YouTube Videos (Hindi/English)
Channel	Link
- CodeWithHarry:	https://youtu.be/7wnove7K-ZQ?t=2500	
- Apna College:	https://youtu.be/med2BtChVMA?t=1200	
- freeCodeCamp:	https://youtu.be/rfscVS0vtbw?t=4000	
### 5. Python Official Docs
Topic	Link
- List:https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
- While	https://docs.python.org/3/reference/compound_stmts.html#while