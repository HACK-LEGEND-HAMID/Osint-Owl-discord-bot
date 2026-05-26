# DAY 10: Tuples & Sets - Duplicate Remover

## 📌 Problem Overview

Today you will learn:
1. How to create Tuples `()`
2. How to create Sets `{}`
3. Difference between Tuple and Set
4. How to remove duplicates using Set
5. How to split strings into lists
6. How to strip whitespace from strings

### What is this program doing?
- Taking comma-separated items as input
- Creating a Tuple from the items
- Converting Tuple to Set (automatically removes duplicates)
- Converting back to Tuple (optional)
- Showing original vs unique data
- Counting duplicates removed

---

## 📚 Tuple vs Set Cheatsheet

| Feature | Tuple `()` | Set `{}` |
|---------|------------|----------|
| Ordered | ✅ Yes | ❌ No |
| Mutable | ❌ No (immutable) | ✅ Yes |
| Allows duplicates | ✅ Yes | ❌ No |
| Indexing | ✅ Yes `tuple[0]` | ❌ No |
| Use case | Fixed data | Unique data |

### Tuple Examples
```python
my_tuple = (1, 2, 3, 2, 1)  # (1, 2, 3, 2, 1) - keeps duplicates
print(my_tuple[0])           # 1 (indexing works)
my_tuple[0] = 10             # ERROR! Cannot change
```
### Set Examples
```py
my_set = {1, 2, 3, 2, 1}     # {1, 2, 3} - removes duplicates
print(my_set[0])              # ERROR! No indexing
my_set.add(4)                 # {1, 2, 3, 4} - can add
```
## ❌ Common Errors & Solutions
### Error 1: Missing * operator
```py
# WRONG ❌
print("="50)  # TypeError

# RIGHT ✅
print("=" * 50)  # Multiply string by number
```
### Error 2: Wrong variable name
```python
# WRONG ❌
item = input("Enter items: ")  # Variable 'item'
for item in items.split(","):  # 'items' not defined

# RIGHT ✅
items = input("Enter items: ")  # Variable 'items'
for item in items.split(","):
```
## Error 3: Missing comma in tuple (single element)
```python
# WRONG ❌
my_tuple = my_tuple + (item.strip())  # TypeError: can only concatenate tuple

# RIGHT ✅
my_tuple = my_tuple + (item.strip(),)  # Comma makes it a tuple
```
## Error 4: Wrong function name
```python
# WRONG ❌
unique_set = sat(my_tuple)  # 'sat' not defined

# RIGHT ✅
unique_set = set(my_tuple)  # 'set' is correct
```
### Error 5: Wrong variable name in print
```python
# WRONG ❌
print(f"✅ Unique Tuple    : {unique_tuple}")  # 'unique_tuple' not defined

# RIGHT ✅
print(f"✅ Unique Tuple    : {unique_tuple}")  # Or use 'unique_tup'
```
### Error 6: Wrong function name for len
```python
# WRONG ❌
print(f"🗑️  Duplicates : {lan(my_tuple) - len(unique_tuple)}")  # 'lan' not defined

# RIGHT ✅
print(f"🗑️  Duplicates : {len(my_tuple) - len(unique_tuple)}")  # 'len' is correct
```

## 📚 Resources to Learn (English)
### 1. W3Schools
Topic	Link
- Tuples:	https://www.w3schools.com/python/python_tuples.asp
- Sets:	https://www.w3schools.com/python/python_sets.asp
- Tuple Methods:	https://www.w3schools.com/python/python_tuples_methods.asp
### 2. Programiz
Topic	Link
- Python Tuples:	https://www.programiz.com/python-programming/tuple
- Python Sets	https://www.programiz.com/python-programming/set
### 3. GeeksforGeeks
Topic	Link
- Tuples:	https://www.geeksforgeeks.org/python-tuples/
- Sets:	https://www.geeksforgeeks.org/python-sets/
### 4. YouTube Videos
Channel	Link	
- CodeWithHarry:	https://youtu.be/7wnove7K-ZQ?t=4500	
- Apna College:	https://youtu.be/med2BtChVMA?t=2400	
- freeCodeCamp:	https://youtu.be/rfscVS0vtbw?t=8000	
 
