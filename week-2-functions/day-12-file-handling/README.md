# DAY 12: File I/O - Note App

## 📌 Problem Overview

Today you will learn:
1. How to open files using `open()`
2. How to write to files using `write()`
3. How to read from files using `read()`
4. Different file modes (`r`, `w`, `a`)
5. How to use `with` statement (context manager)
6. How to handle file operations safely

### What is this program doing?
- Creating a simple note-taking application
- Writing new notes to `notes.txt` file
- Reading and displaying all saved notes
- Appending new notes (not overwriting)
- Exiting the program

---

## 📚 File Modes Cheatsheet

| Mode | Description | What it does |
|------|-------------|--------------|
| `"r"` | Read | Read existing file (file must exist) |
| `"w"` | Write | Overwrites file or creates new |
| `"a"` | Append | Adds to end of file or creates new |
| `"x"` | Create | Creates new file (error if exists) |
| `"r+"` | Read/Write | Read and write to file |

### File Operations Examples
```python
# WRITE (overwrites)
with open("file.txt", "w") as f:
    f.write("Hello")      # Writes "Hello"

# APPEND (adds to end)
with open("file.txt", "a") as f:
    f.write("World")      # Adds "World" after existing content

# READ (reads entire file)
with open("file.txt", "r") as f:
    content = f.read()    # Gets all content as string

# READ LINE BY LINE
with open("file.txt", "r") as f:
    for line in f:
        print(line)       # Prints each line
```
## ❌ Common Errors & Solutions
### Error 1: Comparing string with integer
```py
# WRONG ❌
if choice == 1:  # '1' is string, 1 is integer

# RIGHT ✅
if choice == '1':  # Compare string with string
```

### Error 2: Wrong variable name
```py
# WRONG ❌
file.write(notes + "\n")  # 'notes' not defined, should be 'note'

# RIGHT ✅
file.write(note + "\n")   # 'note' is the variable
```

### Error 3: Typo in method name
```python
# WRONG ❌
notes = file.reed()  # 'reed' not a method

# RIGHT ✅
notes = file.read()  # 'read' is correct
```
### Error 4: Typo in break statement
```python
# WRONG ❌
broke  # 'broke' is not a keyword

# RIGHT ✅
break  # 'break' is correct
```
### Error 5: File not found when reading
```python
# WRONG ❌ (if file doesn't exist)
with open("notes.txt", "r") as file:  # FileNotFoundError

# RIGHT ✅ (handle with try-except)
try:
    with open("notes.txt", "r") as file:
        notes = file.read()
except FileNotFoundError:
    notes = "No notes yet!"
```
### Error 6: Using wrong mode
```python
# WRONG ❌ (overwrites existing notes)
with open("notes.txt", "w") as file:  # 'w' overwrites!

# RIGHT ✅ (adds to existing notes)
with open("notes.txt", "a") as file:  # 'a' appends
```

## 📚 Resources to Learn (English)
### 1. W3Schools
Topic	Link
- File Handling:	https://www.w3schools.com/python/python_file_handling.asp
- File Write:	https://www.w3schools.com/python/python_file_write.asp
- File Read:	https://www.w3schools.com/python/python_file_read.asp
### 2. Programiz
Topic	Link
- File I/O:	https://www.programiz.com/python-programming/file-operation
- With Statement:	https://www.programiz.com/python-programming/context-manager
### 3. GeeksforGeeks
Topic	Link
- File Handling:	https://www.geeksforgeeks.org/file-handling-python/
- Open Function:	https://www.geeksforgeeks.org/open-function-python/
### 4. YouTube Videos
Channel	Link
- CodeWithHarry:	https://youtu.be/7wnove7K-ZQ?t=5500	
- Apna College:	https://youtu.be/med2BtChVMA?t=3000	
- freeCodeCamp	https://youtu.be/rfscVS0vtbw?t=10000