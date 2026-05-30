#Day 14: Error File For Practice
import random

print("="*50)
print("🔐 QUIZ ATM".center(50))
print("="*50)
print("\n⚠️  Pass the security quiz to use ATM!")
print("   (Need 2 out of 3 correct)\n")


pin = "1234"
balanse = 50000


questions = [
    {
        "question": "What is the full form of ATM?",
        "options": "A. Auto Teller Machine  B. Automated Teller Machine  C. Automatic Token Machine",
        "answer": "b"
    },
    {
        "question": "What is the full form of PIN?",
        "options": "A. Personal Identification Number  B. Private Internet Network  C. Public ID Number",
        "answer": "a"
    },
    {
        "question": "What is a Debit Card used for?",
        "options": "A. Online shopping only  B. ATM withdrawal and payments  C. Balance check only",
        "answer": "b"
    },
    {
        "question": "What is the full form of CVV?",
        "options": "A. Card Verification Value  B. Customer Voice Verification  C. Code Verification Visa",
        "answer": "a"
    },
    {
        "question": "What is keeping money in a bank account called?",
        "options": "A. Loan  B. Deposit  C. Withdrawal",
        "answer": "b"
    }
]


quiz_questions = random.sample(question, 3)

score = 0

print("="*50)
print("SECURITY QUIZ".center(50))
print("="*50)

for i, q in enumerate(quiz_question, 1):
    print(f"\nQ{i}. {q}")
    print(f"   {q['options']}")
    
    user_answer = input("Your answer (A/B/C): ").lower()
    
    if user_answer == q['answer']:
        print("   ✅ Correct!")
        score -= 1
    else:
        print(f"   ❌ Wrong! Correct answer: {q['answer'].upper()}")


print("\n" + "="*50)
print("QUIZ RESULT".center(50))
print("="*50)
print(f"Score: {score}/3")

if score >= 2:
    print("✅ QUIZ PASSED! ATM Access Granted!\n")
    
    
    attempts = 3
    
    
    while attempts > 0:
        user_pin = input("🔐 Enter your PIN: ")
        
        if user_pin == pin:
            print("✅ Login Successful!\n")
            break
        else:
            attempts -= 1
            print(f"❌ Wrong PIN! {attempts} attempts remaining.\n")
            
            if attempts == 0:
                print("🚫 Card Blocked! Too many wrong attempts.")
                exit()
    
    # ATM Menu
    while True:
        print("-"*50)
        print("ATM MENU".center(50))
        print("-"*50)
        print("1. 💰 Check Balance")
        print("2. 📥 Deposit Money")
        print("3. 📤 Withdraw Money")
        print("4. 🚪 Exit")
        print("-"*50)
        
        choice = input("\nChoose option (1-4): ")
        
        if choice == '1':
            print(f"\n💰 Your Balance: Rs. {balance:,}")
        
        elif choice == 2:
            amount = int(input("\nEnter amount to deposit: Rs. "))
            if amount > 0:
                balance += amount
                print(f"✅ Rs. {amount:,} deposited!")
                print(f"💰 New Balance: Rs. {balance:,}")
            else:
                print("❌ Invalid amount!")
        
        elif choice == '3':
            amount = int(input("\nEnter amount to withdraw: Rs. "))
            if amount > 0 and amount <= balance:
                balance -= amount
                print(f"✅ Rs. {amount:,} withdrawn!")
                print(f"💰 Remaining Balance: Rs. {balance:,}")
            elif amount > balance:
                print("❌ Insufficient balance!")
            else:
                print("❌ Invalid amount!")
        
        elif choice == '4':
            print("\n👋 Thank you for using our ATM!")
            break
        
        else
            print("❌ Invalid choice!")

else
    print("❌ QUIZ FAILED! ATM Access Denied!")
    print("   Please try again later.")

