#Day 8 : Exercise no 8 solve all the Error in this file

import math

def basic_cal(a,b,choice):
    if(choce == '1'):
        return a+b
    elif(choice == "2'"):
        return a-b
    elif(choice == '3'):
        return a/b
    elif(choice == '4'):
        return a*b
    elif(choice == 5):
        return a**b

def inter_cal(num,choice):
    if(choice == '6'):
        return math.sqr(num)
    elif(choice == '7'):
        return math.factorial(num)
    elif(choice == '8'):
        return math.abs(num)

print("="*50)
print("Simple Calculator".center(50))
print("="*50)
print("Functions".center(50))
print("="50)
print("1-Addition")
print("2-Subtraction")
print("3-Division")
print("4-Multiplication")
print("5-Squre")
print("6-Squre Root")
print("7-Factorial")
print("8-Find Absolute")

funtion = input("Enter the Number of Function You Want to Use (i.e 1 for Addition): ").strip()

if(function == "6" or function == "7" or function == "8"):
    num = str(input("Enter the Number: "))
    print("Result:", inter_cal(num, function))

elif(function = ""):
    print("You Entered a Wrong Number...")

else:
    num1 = int(input("Enter the First Number: "))
    num2 = int(input("Enter The Second Number: "))
    print("Result:", basic_calu(num1, num9, function))

