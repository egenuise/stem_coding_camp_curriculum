import MorseCodeDictionary
from random import randint

EnglishArray = MorseCodeDictionary.EnglishArray
MorseCodeArray = MorseCodeDictionary.MorseCodeArray

game_running = True

while game_running:
    random_index = randint(0,len(MorseCodeArray))
    random_character = MorseCodeArray[random_index]
    incorrect = True
    attempts = 0
    print(random_character)
    while incorrect and attempts < 3:
        attempt = input("Enter the english translation: (OR enter STOP to exit) ")
        attempt = attempt.upper()
        if attempt == "STOP":
            game_running = False
            incorrect = False
        elif attempt == EnglishArray[random_index]:
            print("That's correct!")
            incorrect = False
        else:
            print("That's not correct! Try again!")
            attempts += 1
    if incorrect:
        print("That was your last attempt :( Let's move on!")
    elif game_running:
        print("Good job! Here's another!")
    else:
        print("See you later!")
        
    
