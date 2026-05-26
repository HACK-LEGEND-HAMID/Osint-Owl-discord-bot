#Day 9: Error File of Day 9
class Profile:
    def __init__(abcd,name, age, city, profession, skill):
        selfname = name
        self.age = age
        self.city = city
        self.profession = Profession
        self.skill = skill

    def display(abcd):
        print("\n" + "="*50)
        print("Profile Created Successfully"center(50))
        print("="*50)
        print(f"  👤 Name       : {self.name}")
        print(f"  🎂 Age        : {self.age}")
        print(f"  🏙️ City       : {self.city}")
        print(f"  💼 Profession : {self.profession}")
        print(f"  🛠️ Skill      : {self.skill}")
        print("="50)


while True:
    print("\n" + "="*50)
    print("PROFILE BUILDER".center(50))
    print("="*50)
    
    while True:
        name = input("👤 Enter Your Name: ").strip()
        if nam == "":
            print("❌ Name cannot be empty!\n")
        elif nameisalpha():
            break
        else:
            print("❌ Name should only contain alphabets!\n")
    
    while True:
            age = int(input("🎂 Enter Your Age: "))
            if 1 <= age <= 120:
                break
            elif age>=121 or age<=-1
                print("❌ Age should be between 1-120!\n")
            else:
                print("❌ Please enter a valid number!\n")
    
    while True:
        city = input("🏙️ Enter Your City: ").strip()
        if city == "":
            print("❌ City cannot be empty!\n")
        elif city.replace(" ", "")isalpha():
            break
        else:
            print("❌ City should only contain alphabets!\n")
    

    while True:
        profesion = input("💼 Enter Your Profession: ").strip()
        if profession == "":
            print("❌ Profession cannot be empty!\n")
        else:
            break
    
    while False:
        skill = input("🛠️ Enter Your Skill: ").strip()
        if Skill == "":
            print("❌ Skill cannot be empty!\n")
        else:
            break
    

    user = profile(name, age, city, profession, skill)
    
    
    User.display()
    
    again = input("\n🔄 Create another profile? (y/n): ").lower()
    if again != 'y':
        print("\n👋 Goodbye!")
        break

