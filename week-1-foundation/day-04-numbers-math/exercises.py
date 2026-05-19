#Day 4:Exercise no 4:- Solve All the Error of this file...
import random

print("="*40)
print("DICE ROLLER".cente(40))
print("="40)

input("\nPress ENTER to Roll the dice...")

dice = random.randint(1, 6)

dice_faces = {
    1 """
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

printf(dice_faces[dice])
print(f"You rolled: [dice]")
