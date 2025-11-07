from random import randrange
from datetime import datetime
while True:
    weather=randrange(10,40)
    date=datetime.now()
    print(f"\nDate & Time: {date.strftime('%Y-%m-%d %H:%M:%S')}")
    if  weather < 15:
        print(f"Weather is Snowy☃️☃️...{weather}")
        
    elif 15 <=weather  < 25:
        print(f"Weather is  Cloudy ☁️☁️....{weather}")
        
    elif 26 <= weather < 40:
        print(f"Weather is Sunny 🌅🌅🌅.....{weather}")

    else:
        Print("Weather not Accuess....")
        
    choice = input("\nDo you want to continue? (Y/N): ").strip().upper()
    if choice == "Y":
        continue
    else:
        print("STOP the code.....")
        break