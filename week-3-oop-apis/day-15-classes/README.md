# DAY 15: Classes & OOP - Bank System

## 📌 Problem Overview

Today you will learn:
1. How to create classes using `class`
2. How to use `__init__` constructor
3. How to create methods inside class
4. How to use `self` parameter
5. How to create objects from class

### What is this program doing?
- Creating bank accounts with random account numbers
- Depositing and withdrawing money
- Checking balance
- PIN verification
- Multiple accounts management

---

## ❌ Common Errors & Solutions

### Error 1: Variable name typo
```python
# WRONG ❌
if amout > 0:  # 'amout' not 'amount'

# RIGHT ✅
if amount > 0:
```
### Error 2: Method name typo
```py
# WRONG ❌
def withdrw(self, amount):  # 'withdrw' wrong spelling

# RIGHT ✅
def withdraw(self, amount):
```
### Error 3: Class name wrong case
```py
# WRONG ❌
acc = Bankaccount(name, deposit)  # 'Bankaccount' small 'a'

# RIGHT ✅
acc = BankAccount(name, deposit)  # 'BankAccount' capital 'A'
```
### Error 4: Missing self parameter
```py
# WRONG ❌
def login():  # Missing self

# RIGHT ✅
def login(self):  # self required
```
### Error 5: String vs integer comparison
```py
# WRONG ❌
if choice == 1:  # '1' is string, 1 is integer

# RIGHT ✅
if choice == '1':  # Compare string with string
```
### Error 6: Variable name mismatch
```py
# WRONG ❌
print(self.current.deposit(amt))  # 'amt' not defined, should be 'amount'

# RIGHT ✅
print(self.current.deposit(amount))
```
### Error 7: Wrong method name
```py
# WRONG ❌
print(self.current.withdraw(amt))  # 'withdraw' is correct

# RIGHT ✅
print(self.current.withdraw(amt))
```
### Error 8: Assignment instead of comparison
```py
# WRONG ❌
if choice = '1':  # = is assignment

# RIGHT ✅
if choice == '1':  # == is comparison
```
### Error 9: Colon after break
```py 
# WRONG ❌
break:  # No colon after break

# RIGHT ✅
break  # No colon
```
### Error 10: Variable name typo in deposit
```py
# WRONG ❌
amount = int(input("Amount: Rs."))
print(self.current.deposit(amt))  # 'amt' vs 'amount'

# RIGHT ✅
amount = int(input("Amount: Rs."))
print(self.current.deposit(amount))
```

## 📚 Resources to Learn
Topic	Link
- Python Classes:	https://www.w3schools.com/python/python_classes.asp
- init Method:	https://www.w3schools.com/python/gloss_python_class_init.asp
- Self Parameter:	https://www.w3schools.com/python/gloss_python_self.asp