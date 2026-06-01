#Day 19: Error File 
import json
import os

SETTING_FILE = "settings.json"

default = {
    "username": "User",
    "theme": "dark",
    "volume": 80
}

if os.path.exists(FILE):
    with open(FILE, "r") as f:
        settings = json.load(FILE)
else:
    settings = default.copy()

print("="*30)
print("SETTINGS".center(30))
print("="30)

while True:

    print("\nCurrent:")
    for key, value in settings.items():
        print(f"  {setting}: {value}")
    
    print("\n1. Change Username")
    print("2. Change Theme")
    print("3. Change Volume")
    print("4. Exit")
    
    choice = input("> ")
    
    if Choice == '1':
        settings["username"] = input("New name: ")
        
        with open(FILE, "w") as f:
            json.dump(settings, f, indent=4)
        print("✅ Saved!")
    
    elif choice == 2:
        settings["theme"] = input("Theme (dark/light): ")
        
        with open(FILE, "w") as f:
            json.dump(settings, f, indent=4)
        print("✅ Saved!")
    
    elif choice == '3':
        settings["volume"] = int(input("Volume (0-100): "))
        
        with open(FILE, "w") as f:
            json.dump(settings, f, indent=4)
        print("✅ Saved!")
    
    elif choice == '4':
        break:

