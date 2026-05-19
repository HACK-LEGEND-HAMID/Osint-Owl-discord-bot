#Day 4:Dice Roller Demo
import random

print("="*40)
print("DICE ROLLER".center(40))
print("="*40)

input("\nPress ENTER to Roll the dice...")

dice = random.randint(1, 6)

dice_faces = {
    1: """
┌─────────┐
│         │
│    ●    │
│         │
└─────────┘""",
    2: """
┌─────────┐
│  ●      │
│         │
│      ●  │
└─────────┘""",
    3: """
┌─────────┐
│  ●      │
│    ●    │
│      ●  │
└─────────┘""",
    4: """
┌─────────┐
│  ●   ●  │
│         │
│  ●   ●  │
└─────────┘""",
    5: """
┌─────────┐
│  ●   ●  │
│    ●    │
│  ●   ●  │
└─────────┘""",
    6: """
┌─────────┐
│  ●   ●  │
│  ●   ●  │
│  ●   ●  │
└─────────┘"""
}

print(dice_faces[dice])
print(f"You rolled: {dice}")

