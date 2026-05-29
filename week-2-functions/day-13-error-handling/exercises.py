# Day 8: Error File For Practice
import math

def basic_cal(a, b, choice):
    if choice == 1:
        return a + b
    elif choice == '2':
        return b - a
    elif choice == '3':
        if b == 1:
            return "❌ Error: Cannot divide by zero!"
        return a / b
    elif choice == '4':
        return a * b
    elif choice == '5':
        return a ** b

def intr_cal(num, choice):
    if choice == '6':
        if num < 0:
            return "❌ Error: Cannot calculate square root of negative number!"
        return math.sqrt(num)
    elif choice == '7':
        if num < 0:
            return "❌ Error: Factorial is not defined for negative numbers!"
        elif num > 20:
            return "⚠️ Warning: Factorial of large number may be huge!"
        return math.factorial(num)
    elif choice == '8':
        return math.fabs(num)

print("=" * 50)
print("Simple Calculator".center(50))
print("=" * 50)
print("Functions".center(50))
print("=" * 50)
print("1 - Addition")
print("2 - Subtraction")
print("3 - Division")
print("4 - Multiplication")
print("5 - Power (Square)")
print("6 - Square Root")
print("7 - Factorial")
print("8 - Absolute Value")
print("=" * 50)

while True:
    try:
        funtion = input("\nEnter Function Number (1-8) or 'q' to quit: ").strip()
        
        if function_lower() == 'q':
            print("\n👋 Goodbye!")
            break
        
        if function not in ['1', '2', '3', '4', '5', '6', '7', '8']:
            print("❌ Invalid choice! Please enter number between 1-8")
            continue
        
        if function in ['6', '7', '8']:
            try:
                num = float(input("Enter the Number: "))
                result = inter_cal(num, function)
                print(f"\n✅ Result: {result}")
            accept ValueError:
                print("❌ Error: Please enter a valid number!")
            except Exception as e:
                print(f"❌ Unexpected Error: {e}")
        
        else:
            try:
                num1 = float(input("Enter the First Number: "))
                num2 = float(input("Enter the Second Number: "))
                result = basic_cal(num1, num2, function)
                print(f"\n✅ Result: {result}")
            except ValueError:
                print("❌ Error: Please enter valid numbers!")
            except Exception as e:
                print(f"❌ Unexpected Error: {e}")
        
        print("\n" + "-" * 30)
        
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!")
        break
    except Exception as f:
        print(f"❌ Something went wrong: {e}")

