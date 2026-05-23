import random

hangman_stages = [

    """
       ┌─────┐
       │     │
             │
             │
             │
             │
    ─────────┴──""",
    

    """
       ┌─────┐
       │     │
       O     │
             │
             │
             │
    ─────────┴──""",
    
    """
       ┌─────┐
       │     │
       O     │
       │     │
             │
             │
    ─────────┴──""",
    
    """
       ┌─────┐
       │     │
       O     │
      /│     │
             │
             │
    ─────────┴──""",
    
    """
       ┌─────┐
       │     │
       O     │
      /│\\    │
             │
             │
    ─────────┴──""",
    
    
    """
       ┌─────┐
       │     │
       O     │
      /│\\    │
      /      │
             │
    ─────────┴──""",
    
    """
       ┌─────┐
       │     │
       O     │
      /│\\    │
      / \\    │
             │
    ─────────┴──"""
]

words = ["hamid", "king", "legend", "hero", "girl", 
         "law", "dragon", "sea", "apple", "dictionary"]


word = random.choice(words)
guessed = ["_"] * len(word)
wrong_letters = []
wrong_guesses = 0
max_wrong = 6

print("="*50)
print("💀 HANGMAN GAME 💀".center(50))
print("="*50)
print("\nGuess the word or DIE trying!")
print(f"The word has {len(word)} letters.\n")

while wrong_guesses < max_wrong and "_" in guessed:
    
    print(hangman_stages[wrong_guesses])
    

    print("\nWord:", " ".join(guessed))
    
    if wrong_letters:
        print("Wrong letters:",', '.join(wrong_letters))
    
    print(f"Lives left: {'❤️ ' * (max_wrong - wrong_guesses)}")
    
    guess = input("\nGuess a letter: ").lower()
    
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter a single letter!")
        continue
    
    if guess in guessed or guess in wrong_letters:
        print("⚠️  You already guessed that letter!")
        continue
    
    if guess in word:
        print("✅ Correct!")
    
        for i, letter in enumerate(word):
            if letter == guess:
                guessed[i] = guess
    else:
        print("❌ Wrong!")
        wrong_guesses += 1
        wrong_letters.append(guess)
    
    print("-"*50)

print(hangman_stages[wrong_guesses])

if "_" not in guessed:
    print("\n" + "="*50)
    print("🎉 YOU WIN! 🎉".center(50))
    print("="*50)
    print(f"\nThe word was: {word.upper()}")
    print("You survived! 😎")
else:
    print("\n" + "="*50)
    print("💀 GAME OVER! 💀".center(50))
    print("="*50)
    print(f"\nThe word was: {word.upper()}")
    print("You have been hanged! ☠️")

print("="*50)
