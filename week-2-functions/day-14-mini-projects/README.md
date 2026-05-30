# DAY 14: Mini Project - Quiz & ATM System

## 📌 Problem Overview

Today you will learn:
1. How to combine multiple concepts (lists, dictionaries, loops, conditionals)
2. How to use `random.sample()` for random question selection
3. How to create a complete ATM system with PIN verification
4. How to handle user input validation
5. How to manage balance (deposit, withdraw, check balance)

### What is this program doing?
- Security quiz with 5 questions (randomly selects 3)
- Need 2/3 correct to pass
- PIN verification (3 attempts only)
- ATM menu: Check Balance, Deposit, Withdraw, Exit
- Full error handling for invalid inputs

---

## 📚 Concepts Used

| Concept | Where Used |
|---------|-------------|
| List of Dictionaries | Questions storage |
| `random.sample()` | Random quiz selection |
| For Loop | Displaying questions |
| While Loop | PIN attempts, ATM menu |
| If-Elif-Else | All decision making |
| String Methods | `.lower()`, `.upper()` |
| f-strings | Formatted output |
| Error Handling | Input validation |

---

## ❌ Common Errors & Solutions

### Error 1: Variable name mismatch (balance vs balanse)
```python
# WRONG ❌
balanse = 50000  # Typo
print(f"Balance: {balance}")  # Wrong variable

# RIGHT ✅
balance = 50000  # Correct spelling
print(f"Balance: {balance}")
```

### Error 2: Wrong variable name (questions vs question)
```python
# WRONG ❌
quiz_questions = random.sample(question, 3)  # 'question' not defined

# RIGHT ✅
quiz_questions = random.sample(questions, 3)  # 'questions' is correct
```
### Error 3: Missing underscore (quiz_questions vs quiz_question)
```python
# WRONG ❌
for i, q in enumerate(quiz_question, 1):  # 'quiz_question' not defined

# RIGHT ✅
for i, q in enumerate(quiz_questions, 1):  # 'quiz_questions' correct
```
### Error 4: Wrong variable in loop
```python
# WRONG ❌
print(f"\nQ{i}. {q}")  # q is dictionary, can't print directly
print(f"   {q['options']}")  # Wrong access

# RIGHT ✅
print(f"\nQ{i}. {q['question']}")  # Access 'question' key
print(f"   {q['options']}")
```
### Error 5: Score calculation wrong
```python
# WRONG ❌
score -= 1  # Decreases score on correct answer

# RIGHT ✅
score += 1  # Increases score on correct answer
```
### Error 6: Missing colon after else
```python
# WRONG ❌
else  # Missing colon

# RIGHT ✅
else:  # Colon required
```
### Error 7: String vs integer comparison
```python
# WRONG ❌
elif choice == 2:  # '2' is string, 2 is integer

# RIGHT ✅
elif choice == '2':  # Compare string with string
```
### Error 8: Missing try-except for int conversion
```python
# WRONG ❌
amount = int(input("Enter amount: "))  # Crashes if user enters text

# RIGHT ✅
try:
    amount = int(input("Enter amount: "))
except ValueError:
    print("❌ Please enter a valid number!")
    continue
```

## 📚 Resources to Learn (English)
### W3Schools
Topic	Link
- Random Module:	https://www.w3schools.com/python/module_random.asp
- Dictionaries:	https://www.w3schools.com/python/python_dictionaries.asp
- While Loops:	https://www.w3schools.com/python/python_while_loops.asp
### Programiz
Topic	Link
- List of Dictionaries:	https://www.programiz.com/python-programming/list-of-dictionary
- Random Sample:	https://www.programiz.com/python-programming/methods/random/sample
### YouTube Videos
Channel	Link	
- CodeWithHarry:	https://youtu.be/7wnove7K-ZQ
- Apna College:	https://youtu.be/med2BtChVMA	
