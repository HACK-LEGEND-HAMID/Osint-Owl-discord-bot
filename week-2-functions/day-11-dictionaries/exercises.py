#Day 11: Solve All The Error in This File
phonebook = ()

print("="*40)
print("PHONEBOOK".center(40))
print("="40)

while True:
    print("\n1. Add Contact")
    print("2. Search Contact")
    print("3. View All")
    print("4. Delete Contact")
    print"5. Exit")
    
    choice = input("\nChoose (1-5): ")
    
    if choice = '1':
        name = input("Enter name: ")
        number = input("Enter number: ")
        phonebook[name] = number
        print(f"✅ {name} Added!")
        
    elif choice == 2:
        name = input("Enter Name to Search: ")
        if name in phonebook:
            print(f"📱 {name}: {phonebook[name]}")
        else:
            print("❌ Not found!")
            
    elif choice == '3':
        if phonebook:
            print("\n📱 ALL CONTACTS:")
            for name, number in phonebook.items():
                print(f"  {name}: {number}")
        else:
            print("📭 Phonebook empty!")
            
    elif choce == '4':
        name = input("Enter name to delete: ")
        if name in phonebook:
            del phonebook[name]
            print(f"🗑️  {name} deleted!")
        else:
            print("❌ Not found!")
            
    elif choice == '5':
        print("👋 Bye!")
        

