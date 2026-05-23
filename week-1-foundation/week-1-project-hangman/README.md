# 💀 Project Day: Hangman Game in Python

A classic Hangman game with ASCII art, built using Python. Guess the word before the hangman is complete!

---

## 🎮 Game Preview

```
       ┌─────┐
       │     │
       O     │
      /│\    │
      / \    │
             │
    ─────────┴──

Word: p y t h _ n
Wrong letters: a, e, i, o, u
Lives left: ❤️ 
Guess a letter: 
```

---

## 🧠 How to Build (Step by Step)

### Step 1: Import Required Module
```python
import random
```
- `random` module for selecting random word
- Built-in module, no installation needed

---

### Step 2: Create Hangman ASCII Art
```python
hangman_stages = [
    # Stage 0: Empty gallows
    # Stage 1: Head
    # Stage 2: Body
    # Stage 3: One arm
    # Stage 4: Both arms
    # Stage 5: One leg
    # Stage 6: Full body (DEAD)
]
```
**Why list?** 
- Each index = number of wrong guesses
- `hangman_stages[0]` = 0 mistakes (empty)
- `hangman_stages[6]` = 6 mistakes (game over)

---

### Step 3: Define Word List
```python
words = ["python", "hangman", "programming", "computer", "keyboard"]
```
- List of possible words
- Computer picks one randomly

---

### Step 4: Initialize Game Variables
```python
word = random.choice(words)        # Pick random word
guessed = ["_"] * len(word)        # Create dashes: ["_","_","_"]
wrong_letters = []                 # Store wrong guesses
wrong_guesses = 0                  # Count mistakes
max_wrong = 6                      # Maximum allowed mistakes
```

**Variable Purpose Table:**

| Variable | Type | Purpose |
|----------|------|---------|
| `word` | string | Secret word to guess |
| `guessed` | list | Shows dashes + correct letters |
| `wrong_letters` | list | Stores all wrong guesses |
| `wrong_guesses` | int | Counts mistakes (0-6) |
| `max_wrong` | int | Max mistakes allowed |

---

### Step 5: Print Game Header
```python
print("="*50)
print("💀 HANGMAN GAME 💀".center(50))
print("="*50)
print(f"The word has {len(word)} letters.")
```
- `"="*50` → Creates a line of 50 equal signs
- `.center(50)` → Centers text in 50 character width
- `len(word)` → Shows how many letters in word

---

### Step 6: Create Game Loop
```python
while wrong_guesses < max_wrong and "_" in guessed:
```
**Loop runs while:**
- Mistakes < 6 (not dead yet)
- Dashes still exist (word not complete)

---

### Step 7: Display Game State (Inside Loop)
```python
# Show hangman picture
print(hangman_stages[wrong_guesses])

# Show current word progress
print("\nWord:", " ".join(guessed))

# Show wrong letters (if any)
if wrong_letters:
    print(f"Wrong letters: {', '.join(wrong_letters)}")

# Show remaining lives
print(f"Lives left: {'❤️ ' * (max_wrong - wrong_guesses)}")
```

**Key Functions:**
- `" ".join(guessed)` → Joins list with spaces: `p _ _ h _ n`
- `", ".join(wrong_letters)` → Joins with commas: `a, b, c`
- `'❤️ ' * 4` → Repeats heart 4 times: `❤️ ❤️ ❤️ ❤️ `

---

### Step 8: Get User Input (Inside Loop)
```python
guess = input("\nGuess a letter: ").lower()
```
- `.lower()` → Converts to lowercase (case-insensitive)

---

### Step 9: Validate Input (Inside Loop)
```python
# Check if single letter
if len(guess) != 1 or not guess.isalpha():
    print("❌ Please enter a single letter!")
    continue

# Check if already guessed
if guess in guessed or guess in wrong_letters:
    print("⚠️  You already guessed that letter!")
    continue
```

**Validation Checks:**
1. `len(guess) != 1` → Must be exactly 1 character
2. `not guess.isalpha()` → Must be a letter (not number/symbol)
3. `guess in guessed` → Already guessed correctly?
4. `guess in wrong_letters` → Already guessed wrong?

---

### Step 10: Check Guess (Inside Loop)
```python
if guess in word:
    print("✅ Correct!")
    for i, letter in enumerate(word):
        if letter == guess:
            guessed[i] = guess
else:
    print("❌ Wrong!")
    wrong_guesses += 1
    wrong_letters.append(guess)
```

**If CORRECT:**
- `enumerate(word)` → Gives position number and letter
- `guessed[i] = guess` → Replaces dash with letter at correct position

**If WRONG:**
- `wrong_guesses += 1` → Increment mistake counter
- `wrong_letters.append(guess)` → Add to wrong guesses list

---

### Step 11: Game Over Screen (After Loop)
```python
print(hangman_stages[wrong_guesses])

if "_" not in guessed:
    print("🎉 YOU WIN! 🎉")
else:
    print("💀 GAME OVER! 💀")
    print("You have been hanged! ☠️")

print(f"The word was: {word.upper()}")
```

**Win Condition:** `"_" not in guessed` → No dashes left
**Lose Condition:** Loop ends but dashes remain → 6 mistakes made

---

## 🔑 Key Concepts Used

| Concept | Where Used |
|---------|------------|
| `import random` | To pick random word |
| `list` | Store hangman stages, words, guessed letters |
| `while loop` | Main game loop |
| `if-elif-else` | Check conditions |
| `enumerate()` | Get position of each letter |
| `join()` | Display list as string |
| `input()` | Get user guess |
| `.lower()` | Case insensitive input |
| `.isalpha()` | Validate letter input |
| `.center()` | Center align text |

---

## 🎯 Functions Used Summary

| Function | Purpose | Example |
|----------|---------|---------|
| `random.choice()` | Pick random item | `random.choice(words)` |
| `len()` | Get length | `len(word)` |
| `enumerate()` | Number + value | `enumerate(word)` |
| `" ".join()` | Join with space | `" ".join(['a','b'])` → `"a b"` |
| `", ".join()` | Join with comma | `", ".join(['a','b'])` → `"a, b"` |
| `.lower()` | To lowercase | `"A".lower()` → `"a"` |
| `.isalpha()` | Check if letter | `"a".isalpha()` → `True` |
| `.center()` | Center text | `"Hi".center(10)` |
| `.append()` | Add to list | `list.append(item)` |

---

## 🚀 How to Run

```bash
# Clone or download the file
python hangman.py
```

---

## 📁 File Structure

```
hangman-game/
│
├── hangman.py          # Main game file
├── README.md           # This file
└── .gitignore
```

---

## 🎮 Sample Gameplay

### Win:
```
Word: _ _ _ _ _ _
Lives left: ❤️ ❤️ ❤️ ❤️ ❤️ ❤️ 
Guess a letter: p
✅ Correct!

Word: p _ _ _ _ _
Guess a letter: y
✅ Correct!

... (continues until word complete)

🎉 YOU WIN! 🎉
The word was: PYTHON
```

### Lose:
```
Word: _ _ t _ _ n
Wrong letters: a, e, i, o, u
Lives left: ❤️ 
Guess a letter: s
❌ Wrong!

       ┌─────┐
       │     │
       O     │
      /│\    │
      / \    │
             │
    ─────────┴──

💀 GAME OVER! 💀
The word was: PYTHON
```

---

## ⚙️ Customization

- **Add more words:** Edit the `words` list
- **Change difficulty:** Modify `max_wrong` (e.g., 4 for hard, 8 for easy)
- **Add hints:** Show category or first letter

---

## 📝 License

Free to use and modify! 🆓

---

Happy Coding! 🎮💀