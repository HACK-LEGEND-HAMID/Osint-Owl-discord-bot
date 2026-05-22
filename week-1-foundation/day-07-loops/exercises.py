#Day 7:Exercise 7 Solve all the error of this file...

import random

print("="50)
print("Welcome to Number Guessing Game!".center(50))
print("="*50)

attempt=0
max_attempt=10
number=random.radint(1,100)

while atempt<max_attempt:
    guess=int(input("Enter Number Between 1 - 100:"))
    attempt+=1

    if Guess==number:
        print(f"\n🎉 Correct! You took {attempts} attempts.")
        break
    elif guess<Number:
        print("Too Low!")
    elif guess>number:
        print("Too High!")

    if attempt == 7:
        print("⚠️  3 attempts left!\n")
    elif attempt == 9:
        print("🚨 Last attempt!\n")


if guess != number:
    print("="*50)
    print("❌ YOU FAILED! ❌"center(50))
    print("="*50)
    print(f"\nThe number was: {number}")
    print("\n☠️  TODAY IS YOUR UNLUCKY DAY! ☠️")
    print("💀 DEATH CAN HAPPEN ANYTIME! 💀")
    print("\nBetter luck next time...")

