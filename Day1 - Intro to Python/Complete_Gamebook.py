# Gamebook
# This is a skeleton code file to help you with your decision story game

'''
First we want to come up with a story for the user to go through.
Then we will add 6 decisions for the user to make throughout the game.
And we will be printing throughout to give the user the proper story.
'''

"TO WIN: R, R, F, L/R"

# First print any introduction details that you want to have in your code
# This could be the start of your story or anything that you want it to be really
print("You've been exploring space and suddenly you find yourself surrounded by asteroids")
print("You have decided that the mission at hand is too important, and there is no turning back now")


# Now we will begin gathering user input for the decisions that they make
# Print a choice of options the user can make to begin their journey
print("You find yourself at an intersection of asteroids")
print("Your only choices are to go left (L) or right (R)")

# Gather user input for their first decision
firstDecision = input("Please choo an option: ")


# check the user's first input
if firstDecision == "L": 
    # print what happens to the user for this decision, let's make this a wrongchoice
    print("Suddenly a you crash into something under your ship that you could not see!")
    print("Your engine dies and the ship becomes space debris in the asteroid field")
    print("GAME OVER")

elif firstDecision == "R": 
    # let's have this be a successful story outcome
    # print how the story progresses
    print("You head right, and see something shoot just under your space ship")
    print("But now you have another problem...")
    print("A hostile ship has been spotted charging up its cannons")
    
    # give the user a new decision
    print("In the last second you are able to go right (R) or left (L)")
    # get input for the second user decison
    secondDecision = input("Please make a choice: ")

    # check the input
    if secondDecision == "L":
        # let's game over here again
        # print what happens to the user
        print("It seems the enemy guessed that you were going to go left.")
        print("You've been hit,and your shields saved you... but now the enemy is coming in to capture you.")
        print("GAME OVER")

    elif secondDecision == "R":
        # let's progress the story here
        #print how it progresses
        print("The enemy laser misses, seeming like they thought you would go the other way")
        print("An asteroid from the field speeds by and knocks the enemy ship out of control.")
        print("It would appear that you are safe for now...")
        
        # give the user a new decision
        print("...")
        print("As if on cue, a giant serpant space a snake appears out of nowhere!")
        print("Do you want to fight (F) or run (R)?")
        
        #get input fo the third user decision
        thirdDecision = input("please enter a decision: ")

        #check what the user decides
        if thirdDecision == "R":
            # lets do a game over here
            # tell the user how they lost
            print("The serpant space snake was much faster than you anticipated!")
            print("It quickly overtakes you and you find yourself inside the serpants gut...")
            print("Game Over")

        elif thirdDecision == "F": 
            # lets make this success again and progress
            # tell the user what happens
            print("The serpant rushes you to attack with its mouth open.")
            print("You quickly evade and launch a missile into the mouth of the worm-like creature.")
            print("The monster explodes and you are again safe.")
                  
            # present a new decison
            print("A giant asteroid suddenly disappears from the background and you find yourself at the end of the asteroid field.")
            print("You look to the left and see nothing, which in space is the most ideal conditions one could hope for to travel safely.")
            print("To the right is a worm hole.")
            print("You see that now is the last moment you can decide to run or not.")
            print("Do you leave the field and go home (L) or enter the worm hole and see where you go (R)?")

            # get user input
            fourthDecision = input("Please choose an option: ")

            # check what the user decides
            if fourthDecision == "L":
                # ending 1
                print("You exit the asteroid field and proceed home to Earth safely.")
                print("It seems you have made it out of danger and are going to be ok.")
                print("THE END")

            elif fourthDecision == "R":
                # ending 2
                print("Time and space begin to warp around you and don't really understand what you see.")
                print("You feel slightly sick, but the ship seems to be holding out alright.")
                print("You wait to see where you will end up and what your adventure has in store for you now.")
                print("THE END?")

