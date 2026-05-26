# DAY 9: Classes & Objects - Profile Builder

## 📌 Problem Overview

Today you will learn:
1. How to create a class using `class` keyword
2. How to use `__init__` constructor method
3. How to create instance variables using `self`
4. How to create class methods
5. How to create objects from a class
6. Input validation using while loops

### What is this program doing?
- Taking user input for name, age, city, profession, skill
- Validating each input (empty check, alphabets only, age range)
- Creating a Profile object with the data
- Displaying the profile in beautiful format
- Asking user to create another profile

---

## 📚 Class Syntax Cheatsheet

```python
# 1. BASIC CLASS
class MyClass:
    def __init__(self, parameter):
        self.parameter = parameter
    
    def my_method(self):
        return self.parameter

# 2. CREATE OBJECT
obj = MyClass("value")

# 3. ACCESS ATTRIBUTE
print(obj.parameter)

# 4. CALL METHOD
print(obj.my_method())

# 5. EXAMPLE CLASS
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

s1 = Student("Hamid", 20)
s1.display()
```

## ❌ Common Errors & Solutions
### Error 1: Wrong parameter name in init
```py
# WRONG ❌
def __init__(abcd, name, age):  # 'abcd' instead of 'self'
    self.name = name

# RIGHT ✅
def __init__(self, name, age):  # 'self' is standard
    self.name = name
```
### Error 2: Missing dot in self.attribute
```py
# WRONG ❌
def __init__(self, name):
    selfname = name  # Missing dot

# RIGHT ✅
def __init__(self, name):
    self.name = name  # self.name
```
### Error 3: Wrong variable name
```py 
# WRONG ❌
self.profession = Profession  # 'Profession' not defined

# RIGHT ✅
self.profession = profession  # parameter name
```
### Error 4: Missing dot in method call
```py 
# WRONG ❌
print("Text"center(50))  # Missing dot

# RIGHT ✅
print("Text".center(50))  # Dot before center
```
### Error 5: Missing * operator
```py 
# WRONG ❌
print("="50)  # Missing *

# RIGHT ✅
print("=" * 50)  # With *
```
### Error 6: Wrong variable name in condition
```py 
# WRONG ❌
if nam == "":  # 'nam' not defined, should be 'name'

# RIGHT ✅
if name == "":
```
### Error 7: Missing dot in method call
```py
# WRONG ❌
elif nameisalpha():  # Missing dot

# RIGHT ✅
elif name.isalpha():  # Dot before isalpha()
```
### Error 8: Missing colon after elif
```py
# WRONG ❌
elif age>=121 or age<=-1  # Missing colon

# RIGHT ✅
elif age>=121 or age<=-1:  # Colon at end
```
### Error 9: Wrong class name case
```py
# WRONG ❌
user = profile(name, age, city, profession, skill)  # 'profile' small p

# RIGHT ✅
user = Profile(name, age, city, profession, skill)  # 'Profile' capital P
```
### Error 10: Wrong variable name case
```py
# WRONG ❌
User.display()  # 'User' capital U

# RIGHT ✅
user.display()  # 'user' small u
```
### Error 11: Wrong loop condition
```py 
# WRONG ❌
while False:  # Loop will never run

# RIGHT ✅
while True:  # Infinite loop until break
```
### Error 12: Wrong variable name
```py 
# WRONG ❌
if Skill == "":  # 'Skill' capital S

# RIGHT ✅
if skill == "":  # 'skill' small s
```
## 📚 Resources to Learn (English)
### 1. W3Schools
Topic	Link
- Classes & Objects:	https://www.w3schools.com/python/python_classes.asp
- init Method:	https://www.w3schools.com/python/gloss_python_class_init.asp
- Self Parameter:	https://www.w3schools.com/python/gloss_python_self.asp

### 2. Programiz
Topic	Link
- Python OOP:	https://www.programiz.com/python-programming/class
- Constructors:	https://www.programiz.com/python-programming/constructor
### 3. GeeksforGeeks
Topic	Link
- Classes:	https://www.geeksforgeeks.org/python-classes-and-objects/
- Self Parameter:	https://www.geeksforgeeks.org/self-in-python-class/
### 4. YouTube Videos
Channel	Link	
- CodeWithHarry:	https://youtu.be/7wnove7K-ZQ?t=4000	
- Apna College:	https://youtu.be/med2BtChVMA?t=2100	
- freeCodeCamp:	https://youtu.be/rfscVS0vtbw?t=7000	
