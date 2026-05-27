# DAY 11: Dictionaries - Phonebook

## 📌 Problem Overview

Today you will learn:
1. How to create dictionaries `{}`
2. How to add key-value pairs to dictionary
3. How to search for keys using `in` operator
4. How to delete items using `del`
5. How to loop through dictionary using `.items()`

### What is this program doing?
- Creating an empty phonebook dictionary
- Showing menu with 5 options
- Adding contacts (name as key, number as value)
- Searching contacts by name
- Viewing all contacts
- Deleting contacts by name
- Exiting the program

---

## 📚 Dictionary Cheatsheet

```python
# 1. CREATE DICTIONARY
phonebook = {}                    # Empty dictionary
contacts = {"Hamid": "123456", "Ali": "789012"}  # With data

# 2. ADD OR UPDATE
phonebook["Sara"] = "555666"      # Add new contact
phonebook["Hamid"] = "999888"     # Update existing

# 3. ACCESS VALUE
number = phonebook["Hamid"]       # Get value (KeyError if not found)
number = phonebook.get("Hamid")   # Get value (returns None if not found)

# 4. CHECK IF KEY EXISTS
if "Hamid" in phonebook:
    print("Found!")

# 5. DELETE
del phonebook["Hamid"]            # Delete key-value pair

# 6. LOOP THROUGH DICTIONARY
for name, number in phonebook.items():
    print(f"{name}: {number}")

# 7. GET ALL KEYS
names = phonebook.keys()          # dict_keys(['Hamid', 'Ali'])

# 8. GET ALL VALUES
numbers = phonebook.values()      # dict_values(['123456', '789012'])

# 9. LENGTH OF DICTIONARY
count = len(phonebook)            # Number of contacts
```
## ❌ Common Errors & Solutions

### Error 1: Using () instead of {} for dictionary
```python
# WRONG ❌
phonebook = ()  # This is a tuple, not dictionary

# RIGHT ✅
phonebook = {}  # This is a dictionary
```
### Error 2: Missing * operator
```python
# WRONG ❌
print("="40)  # TypeError

# RIGHT ✅
print("=" * 40)  # Multiply string by number
```
### Error 3: Missing parentheses in print
```python
# WRONG ❌
print"5. Exit")  # SyntaxError

# RIGHT ✅
print("5. Exit")  # Parentheses around string
```
### Error 4: Using = instead of == in comparison
```python
# WRONG ❌
if choice = '1':  # Assignment, not comparison

# RIGHT ✅
if choice == '1':  # Comparison
```
### Error 5: Comparing string with integer
```python
# WRONG ❌
elif choice == 2:  # '2' is string, 2 is integer

# RIGHT ✅
elif choice == '2':  # Compare string with string
```
### Error 6: Typo in variable name
```python
# WRONG ❌
elif choce == '4':  # 'choce' instead of 'choice'

# RIGHT ✅
elif choice == '4':  # Correct spelling
```
### Error 7: Missing break in exit
```python
# WRONG ❌
elif choice == '5':
    print("👋 Bye!")  # No break, loop continues

# RIGHT ✅
elif choice == '5':
    print("👋 Bye!")
    break  # Exit the loop
```

## 📚 Resources to Learn (English)
### 1. W3Schools
Topic	Link
- Dictionaries:	https://www.w3schools.com/python/python_dictionaries.asp
- Dictionary Methods:	https://www.w3schools.com/python/python_dictionaries_methods.asp
- Access Items:	https://www.w3schools.com/python/python_dictionaries_access.asp
### 2. Programiz
Topic	Link
- Python Dictionary:	https://www.programiz.com/python-programming/dictionary
- Dictionary Methods:	https://www.programiz.com/python-programming/methods/dictionary
### 3. GeeksforGeeks
Topic	Link
- Dictionaries:	https://www.geeksforgeeks.org/python-dictionary/
- Dictionary Methods:	https://www.geeksforgeeks.org/python-dictionary-methods/
### 4. YouTube Videos
Channel	Link	
- CodeWithHarry:	https://youtu.be/7wnove7K-ZQ?t=5000	
- Apna College:	https://youtu.be/med2BtChVMA?t=2700	
- freeCodeCamp:	https://youtu.be/rfscVS0vtbw?t=9000	