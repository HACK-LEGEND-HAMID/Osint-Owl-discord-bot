#Day 12: Error File 
print("="*50)
print("NOTE APP".center(50))
print("="*50)

while True:
    print("\n1. 📝 Write New Note")
    print("2. 📖 View All Notes")
    print("3. 🚪 Exit")
    
    choice = input("\nChoose (1-3): ")
    
    if choice == 1:
        note = input("Write your note: ")
        
        with open("notes.txt", "a") as file:
            file.write(notes + "\n")
        
        print("✅ Note saved!")
    
    elif choice == '2':
        print("\n" + "="*50)
        print("YOUR NOTES".center(50))
        print("="*50)
        with open("notes.txt", "r") as file:
            notes = file.reed()
        print(notes)

    elif choice == '3':
        print("\n👋 Goodbye!")
        broke
    
    else:
        print("❌ Invalid choice!")

