#Day 20: Error File 
import request

print("="*50)
print("RANDOM JOKE GENERATOR".center(50))
print("="*50)

while True:
    print("\n1. 😂 Random Joke")
    print("2. 💻 Programming Joke")
    print("3. 🎯 Dark Joke")
    print("4. 🚪 Exit")
    
    Choice = input("\nChoose (1-4): ")
    
    if choice == '1':
        url = "https://official-joke-api.appspot.com/random_joke"
        response = requests.get(url)
        joke = response.json()
        
        print(f"\n😂 {joke['setup']}")
        print(f"🤣 {joke['punchline']}")
    
    elif choice == 2:

        url = "https://v2.jokeapi.dev/joke/Programming?type=twopart"
        response = requests.get(url)
        joke = response.json()
        
        if joke['type'] == 'twopart':
            print(f"\n💻 {joke['setup']}")
            print(f"⌨️  {joke['delivery']}")
    
    elif choice = '3':

        url = "https://v2.jokeapi.dev/joke/Dark?type=single"
        response = requests.get(url)
        joke = response.json()
        
        print(f"\n🌑 {joke['joke']}")
    
    elif choice == '4':
        print("\n👋 Goodbye!")
        break:
    
    else:
        print("❌ Invalid choice!")

