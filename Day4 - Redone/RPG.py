# This  is code for a basic text based rpg style game

# we want to import random so that we can have some "luck based damage options"
import random

enemies = ["Chance", "Zach"]

# stats are attack, health,  and defense
stats = {
    "Chance": [6, 30, 3],
    "Zach": [4, 20, 2]
    }

# Create a game running state
game_running = True

# variable to represent if a fight is currently happening
fighting = False

# get some info about the user to make them a character
name = input("Enter your name: ")

# generate some random stats for the player
attack = 8 + random.randint(0, 5)
health = 35 + random.randint(0, 15)
defense = 5 + random.randint(0, 5)

# save original health value
startingHealth = health

# make the enemy variable so it stays in existence
enemy = ""
enemyHealth = 0

# now let's start the loop of the game
while game_running and health > 0:
    if fighting == False:
        print("Would you like to fight an enemy (F) or exit game (X)?")
        choice = input("Please make a decision: ")
        choice = choice.upper()

        # end the game if need be
        if choice == "X":
            game_running = False
            print("See you later!")
            
        # if they want to fight we are going to pick an enemy randomly
        else:
            enemyIndex = random.randint(0, len(enemies) - 1)
            enemy = enemies[enemyIndex]
            enemyHealth = stats[enemy][1]
            print("Oh no! " + enemy + " is approaching you!")
            fighting = True

    else:
        print("The battle is ongoing...")
        print("Would you like to attack with your sword (S) or a fireball (F)?")
        attackStyle = input("Enter a decision: ")
        # if attack chance with fire its double and zach with sword is double as well
        if enemy == "Chance" and attackStyle == "F" and random.randint(0,2) == 1:
            print("The attack was a critical hit! You did " + str(attack * 2) + " damage!")
            enemyHealth = enemyHealth - (2 * attack)
            print("Chance has " + str(enemyHealth) + " remaining...")
            damageTaken = random.randint(0, stats[enemy][0])
            print("Chance does " + str(damageTaken) + " damage!")
            health = health - damageTaken
        elif enemy == "Zach" and attackStyle == "S" and random.randint(0, 2) == 1:
            print("The attack was a critical hit! You did " + str(attack * 2) + " damage!")
            enemyHealth = enemyHealth - (2 * attack)
            print("Zach has " + str(enemyHealth) + " remaining...")
            damageTaken = random.randint(0, stats[enemy][0])
            print("Zach does " + str(damageTaken) + " damage!")
            health = health - damageTaken

        else:
            print("The attack you chose did normal amounts of damage... (" + str(attack) + ")")
            enemyHealth = enemyHealth - attack
            print(enemy + " has " + str(enemyHealth) + " remaining...")
            damageTaken = random.randint(0, stats[enemy][0])
            print(enemy + " does " + str(damageTaken) + " damage!")
            health = health - damageTaken

        if enemyHealth <= 0:
            print("You have won, and your stats have improved!")
            health = startingHealth + 5
            startingHealth = health
            fighting = False
            attack = attack + 3
            defense = defense + 1
        elif health <= 0:
            print("You have been defeated...")
            game_running = False
        else:
            print("You have " + str(health) + " health remaining...")
            print(enemy + " has " + str(enemyHealth) + " health remaining")

            

    # check enemy health less than zero and reset fighting state if so and level up the player and improve
                  



#print(stats[enemy])


