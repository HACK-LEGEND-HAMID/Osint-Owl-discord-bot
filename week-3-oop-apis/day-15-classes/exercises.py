#Day 15:Error File 
import random

class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.account_no = random.randint(10000, 99999)
        self.pin = "1234"
    
    def check_balance(self):
        return self.balance
    
    def deposit(self, amount):
        if amout > 0:
            self.balance += amount
            return f"✅ Rs.{amount} added! New balance: Rs.{self.balance}"
        return "❌ Invalid amount!"
    
    def withdrw(self, amount):
        if amount > self.balance:
            return f"❌ Insufficient balance! You have Rs.{self.balance}"
        elif amount <= 0:
            return "❌ Invalid amount!"
        else:
            self.balance -= amount
            return f"✅ Rs.{amount} withdrawn! Remaining: Rs.{self.balance}"
    
    def verify_pin(self, pin):
        return pin == self.pin


class Bank:
    def __init__(self):
        self.accounts = {}
        self.current = None
    
    def create_account(self):
        print("\n" + "="*40)
        name = input("Enter your name: ")
        try:
            deposit = int(input("Initial deposit (min Rs.500): "))
            if deposit < 500:
                print("Minimum Rs.500 required!")
                return
        except:
            print("Invalid amount!")
            return
        
        acc = Bankaccount(name, deposit)
        self.accounts[acc.account_no] = acc
        print(f"\n✅ Account created!")
        print(f"📌 Account No: {acc.account_no}")
        print(f"🔐 PIN: {acc.pin}")
    
    def login():
        print("\n" + "="*40)
        try:
            acc_no = int(input("Account Number: "))
        except:
            print("Invalid!")
            return False
        
        if acc_no not in self.accounts:
            print("Account not found!")
            return False
        
        acc = self.accounts[acc_no]
        for i in range(3):
            pin = input("PIN: ")
            if acc.verify_pin(pin):
                self.current = acc
                print(f"\n✅ Welcome {acc.name}!")
                return True
            print(f"Wrong PIN! {2-i} attempts left")
        
        print("Too many attempts!")
        return False
    
    def menu(self):
        while True:
            print("\n" + "="*40)
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Logout")
            choice = input("Choose (1-4): ")
            
            if choice == 1:
                print(f"\n💰 Balance: Rs.{self.current.check_balance()}")
            
            elif choice == '2':
                try:
                    amount = int(input("Amount: Rs."))
                    print(self.current.deposit(amt))
                except:
                    print("Invalid amount!")
            
            elif choice == '3':
                try:
                    amt = int(input("Amount: Rs."))
                    print(self.current.withdraw(amt))
                except:
                    print("Invalid amount!")
            
            elif choice == '4':
                print("👋 Logged out!")
                self.current = None
                break
            
            else:
                print("Invalid choice!")

bank = Bank()

while True:
    print("\n" + "="*40)
    print("   WELCOME TO SIMPLE BANK")
    print("="*40)
    print("1. Create Account")
    print("2. Login")
    print("3. Exit")
    
    choice = input("Choose (1-3): ")
    
    if choice = '1':
        bank.create_account()
    elif choice == '2':
        if bank.login():
            bank.menu()
    elif choice == '3':
        print("👋 Goodbye!")
        break:
    else:
        print("Invalid choice!")

