#Day 5: Grade Calculator Demo

percentage = int(input("Enter Your Percentage:"))

if(percentage >= 90 and percentage <=100):
    print("A Grade")
    
elif(percentage >=80 and percentage <=89):
    print("B Grade")
        
elif(percentage >=70 and percentage <=79):
    print("C Grade")
    
elif(percentage >= 60 and percentage <=69):
    print("D Grade")
        
elif(percentage >=50 and percentage <=59):
    print("D Grade")
        
elif(percentage>=101):
    print("Please Enter a Valid Percentage!")
else:
    print("Fail")
