# ============================================
# GRAND PARENT CLASS
# ============================================
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def eat(self):
        print(f"🍽️  {self.name} is eating")
    
    def sleep(self):
        print(f"😴 {self.name} is sleeping")
    
    def info(self):
        print(f"👤 Name: {self.name}, Age: {self.age}")

# ============================================
# CHILD CLASS 1 (Inherits Animal)
# ============================================
def Mammal(Animal):
    def feed_milk(self):
        print(f"🍼 {slf.name} feeds milk to babies")

# ============================================
# CHILD CLASS 2 (Inherits Mammal)
# ============================================
class Dog(Mamal):
    def bark(self):
        print(f"🐕 {self.name} says: Woof Woof!")
    
    def wag_tail(Mamal):
        print(f"🔄 {self.name} is wagging tail")

# ============================================
# CHILD CLASS 3 (Inherits Mammal)
# ============================================
class Cat(Mammal):
    def meow(self):
        print(f"🐱 {self.name} says: Meow Meow!")
    
    def purr(self):
        print(f"💤 {self.name} is purring")

# ============================================
# CHILD CLASS 4 (Inherits Animal directly)
# ============================================
class Bird(Animal):
    def fly(self):
        print(f"🕊️  {self.name} is flying")
    
    def lay_eggs(self):
        print(f"🥚 {self.name} lays eggs")

# ============================================
# USING THE CLASSES
# ============================================
print("="*50)
print("ANIMAL HIERARCHY".center(50))
print("="*50)

# Dog object
print("\n🐕 DOG:")
tomy = Dog("Tommy", 3)
tommy.infor()        
tommy.eat()           
tommy.sleep()       
tommy.feed_mlk()   
tommy.bark()        
tommy.wag_tail()      

# Cat object
print("\n🐱 CAT:")
kitty = Cat("Kitty", 2)
kitty.info()          
kitty.eat() 
kitty.sleep()                      
kitty.feed_milk()
kitty.meow()          
kitty.purr()          

# Bird object
print("\n🕊️  BIRD:")
parrot = Bird("Mithu", 1)
parrot.info()         
parrot.eat()    
parrot.fly()          
parrot.lay_eggs()     

