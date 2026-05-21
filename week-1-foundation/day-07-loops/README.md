# DAY 7: Random Numbers & Loops - Number Guessing Game

## 📌 Problem Overview

Today you will learn:
1. How to use `random.randint()` to generate secret number
2. How to use `while` loop with attempt counter
3. How to use `if-elif-else` for comparing numbers
4. How to track number of attempts
5. How to give hints (Too Low / Too High)
6. How to show remaining attempts warning

### What is this program doing?
- Generating random number between 1 and 100
- Giving user 10 attempts to guess the number
- Telling if guess is Too Low or Too High
- Showing warning at 3 attempts left and last attempt
- Revealing the number if user fails

---

## ❌ Common Errors & Solutions

### Error 1: Missing * operator
```python
# WRONG ❌
print("="50)  # TypeError

# RIGHT ✅
print("=" * 50)  # Multiply string by number
```
### Error 2: Typo in randint
```py
# WRONG ❌
number = random.radint(1, 100)  # 'radint' is wrong

# RIGHT ✅
number = random.randint(1, 100)  # 'randint' is correct
```

### Error 3: Typo in variable name
```py
# WRONG ❌
while atempt < max_attempt:  # 'atempt' missing 't'

# RIGHT ✅
while attempt < max_attempt:  # 'attempt' is correct
```
### Error 4: Wrong case in variable
```py
# WRONG ❌
if Guess == number:  # 'Guess' with capital G, variable is 'guess'

# RIGHT ✅
if guess == number:  # 'guess' with small g
```

### Error 5: Wrong variable name (attempts vs attempt)
```py
# WRONG ❌
print(f"\n🎉 Correct! You took {attempts} attempts.")  # 'attempts' not defined

# RIGHT ✅
print(f"\n🎉 Correct! You took {attempt} attempts.")  # 'attempt' is correct
```
### Error 6: Spelling mistakes in messages
```py
# WRONG ❌
print("To Low!")   # Should be 'Too'
print("To High!")  # Should be 'Too'

# RIGHT ✅
print("Too Low!")   # Correct spelling
print("Too High!")  # Correct spelling
```
### Error 7: Missing dot in center method
```py
# WRONG ❌
print("❌ YOU FAILED! ❌"center(50))  # Missing dot

# RIGHT ✅
print("❌ YOU FAILED! ❌".center(50))  # Dot before center
```
## 📚 Resources to Learn (English)

### 1. W3Schools (Best for beginners)
Topic	Link
- Random Module:	https://www.w3schools.com/python/module_random.asp
- While Loops:	https://www.w3schools.com/python/python_while_loops.asp
- If Else:	https://www.w3schools.com/python/python_conditions.asp
### 2. Programiz (Simple explanations)
Topic	Link
- Random Number	https://www.programiz.com/python-programming/modules/random
- While Loop	https://www.programiz.com/python-programming/while-loop
### 3. GeeksforGeeks (Detailed)
Topic	Link
- randint()	https://www.geeksforgeeks.org/python-randint-function/
- Guessing Game	https://www.geeksforgeeks.org/number-guessing-game-in-python/
### 4. YouTube Videos (Hindi/English)
Channel	Link
- CodeWithHarry:	https://youtu.be/7wnove7K-ZQ?t=3000	Guessing Game
- Apna College:	https://youtu.be/med2BtChVMA?t=1500	Random Numbers
- freeCodeCamp:	https://youtu.be/rfscVS0vtbw?t=5000	Game Project
### 5. Python Official Docs
Topic	Link
- random.randint	https://docs.python.org/3/library/random.html#random.randint