class Profile:
    def __init__(self, name, age, city, profession, skill):
        self.name = name
        self.age = age
        self.city = city
        self.profession = profession
        self.skill = skill

    def display(self):
        print("\n" + "="*50)
        print("Profile Created Successfully".center(50))
        print("="*50)
        print(f"  👤 Name       : {self.name}")
        print(f"  🎂 Age        : {self.age}")
        print(f"  🏙️ City       : {self.city}")
        print(f"  💼 Profession : {self.profession}")
        print(f"  🛠️ Skill      : {self.skill}")
        print("="*50)

while True:
    print("\n" + "="*50)
    print("PROFILE BUILDER".center(50))
    print("="*50)
    

    while True:
        name = input("👤 Enter Your Name: ").strip()
        if name == "":
            print("❌ Name cannot be empty!\n")
        elif name.isalpha():
            break
        else:
            print("❌ Name should only contain alphabets!\n")
    

    while True:
        try:
            age = int(input("🎂 Enter Your Age: "))
            if 1 <= age <= 120:
                break
            else:
                print("❌ Age should be between 1-120!\n")
        except ValueError:
            print("❌ Please enter a valid number!\n")
    

    while True:
        city = input("🏙️  Enter Your City: ").strip()
        if city == "":
            print("❌ City cannot be empty!\n")
        elif city.replace(" ", "").isalpha():
            break
        else:
            print("❌ City should only contain alphabets!\n")

    while True:
        profession = input("💼 Enter Your Profession: ").strip()
        if profession == "":
            print("❌ Profession cannot be empty!\n")
        else:
            break
    
    while True:
        skill = input("🛠️  Enter Your Skill: ").strip()
        if skill == "":
            print("❌ Skill cannot be empty!\n")
        else:
            break
    
    user = Profile(name, age, city, profession, skill)
    
    user.display()
    
    again = input("\n🔄 Create another profile? (y/n): ").lower()
    if again != 'y':
        print("\n👋 Goodbye!")
        break
