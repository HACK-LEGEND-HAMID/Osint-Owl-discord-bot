#Day 2: Simple Age Calculator Demo
birth_year=int(input("Enter Your Birh Month (i.e 2000):"))
current_year=int(input("Enter the Current Year:"))

age = current_year - birth_year

print("=" * 30)
print("     AGE CALCULATOR")
print("=" * 30)
print(f"Current Year: {current_year}")
print(f"Birth Year: {birth_year}")
print(f"Your Age is: {age} years")
print("=" * 30)
