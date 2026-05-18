#Day 3: Text formatter Demo FIle.
import textwrap

print("="*50)
print("TEXT FORMATTER".center(50))
print("="*50)

text = input("\nEnter your text: ")

# Show all formats
print("\n" + "="*50)
print("ALL FORMATS".center(50))
print("="*50)

print("\n1. UPPERCASE:")
print(text.upper())

print("\n2. lowercase:")
print(text.lower())

print("\n3. Title Case:")
print(text.title())

print("\n4. Capitalize First Letter:")
print(text.capitalize())

print("\n5. Remove Extra Spaces:")
print(" ".join(text.split()))

print("\n6. Word Wrap (50 chars):")
print(textwrap.fill(text, width=50))

print("\n7. Center Aligned:")
print(text.center(70))

print("\n8. Right Aligned:")
print(text.rjust(70))

print("\n9. Left Aligned:")
print(text.ljust(70))

print("\n10. Swap Case (UPPER⇄lower):")
print(text.swapcase())

print("\n11. Reversed Text:")
print(text[::-1])

print("\n12. Words Count:")
words = text.split()
print(f"Total Words: {len(words)}")
print(f"Total Characters: {len(text)}")

print("\n" + "="*50)
print("DONE!".center(50))
print("="*50)
