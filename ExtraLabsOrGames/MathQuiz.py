'''
Math Quiz - Lab 3
Jordan Nickell and Zach Messenger
jcn85 and zam48
CS 126 Section 3
9-28-17
'''

# Math Quiz

# We started by importing random integer
from random import randint

print("Welcome to Math Quiz!")
print("=====================\n")

# User input for level
math_level = input("Choose beginner, intermediate, or advanced: ").lower()
# User input for number of questions
runtime = input("How many questions do you want? ")

# This section of the code is for a 'beginner' quiz
if math_level == 'beginner':
    # We set the correct number at the start of each different quiz
    correct = 0
    # This is the basic loop for the correct number of questions
    for i in range(0, int(runtime)):
        # Here we set operands to be randomly created for each question
        x = randint(1, 10)
        y = randint(1, 10)
        # We also added some randomness to the addition or subtraction
        z = randint(1, 2)
        if z == 1:
            z = '-'
            actual = x - y
        elif z == 2:
            z = '+'
            actual = x + y
        # This prints the problem number and the question for the user
        # The '+ 1' makes the labels for the problems start on 1
        print("Problem " + str(i + 1))
        print("%d %s %d" % (x, z, y))
        ans = input("What is the answer? ")
        # This checks the user's answers and updates their score
        if float(ans) == actual:
            print("You got it!")
            correct += 1
        else:
            print("You missed that one...")
    # This calculates the user's scores and displays it to them
    percent_correct = correct/int(runtime) * 100
    print("You got %.02f percent right" % percent_correct)


# This section of code is for an 'intermediate' quiz
elif math_level == 'intermediate':
    # Again the correct counter has been set to zero
    correct = 0
    # This is so the user knows what to do with long decimals
    print("Round division questions to 2 decimals.")
    # The basic loop is here again
    for i in range(0, int(runtime)):
        # Added the random integers with an increased range
        x = randint(1, 25)
        y = randint(1, 25)
        # This is for randomly creating operators for each question
        z = randint(1, 4)
        if z == 1:
            z = '-'
            actual = x - y
        elif z == 2:
            z = '+'
            actual = x + y
        elif z == 3:
            z = '*'
            actual = x * y
        elif z == 4:
            z = '/'
            actual = x / y
            # The rounding here is so the answer won't be wrong
            actual = round(actual, 2)
        # This prints problem and question for the user
        # Again "+ 1" is for the Problem number starting on 1 not 0
        print("Problem " + str(i + 1))
        print("%d %s %d" % (x, z, y))
        ans = input("What is the answer? ")
        # This checks the users answers and keeps their score
        if float(ans) == actual:
            print("You got it!")
            correct += 1
        else:
            print('You missed that one...')
    # This calculates the user's score and shows them
    percent_correct = correct/int(runtime) * 100
    print("You got %.02f percent right" % percent_correct)


# This section of code is for an 'advanced' quiz
elif math_level == 'advanced':
    # Set the number of problems correct at the start
    correct = 0
    # So the user knows what to do with long decimals
    print("Round division questions to 2 decimals.")
    # Again the basic loop
    for i in range(0, int(runtime)):
        # These are three operands used in the problems
        # They are all randomized and have the same range
        x = randint(1, 25)
        y = randint(1, 25)
        v = randint(1, 25)
        # This variable will be for all exponents
        w = randint(0, 5)
        # This variable detrmines which question will be displayed
        z = randint(1, 5)
        # Within every question rounding happens too
        # The first possible question
        if z == 1:
            a = str(x) + ' * ' + str(y) + ' / ' + str(v)
            actual = x * y / v
            actual = round(actual, 2)
        # The second possible question
        elif z == 2:
            a = str(x) + ' ** ' + str(w) + ' / ' + str(v)
            actual = x ** w / v
            actual = round(actual, 2)
        # The third possible question
        elif z == 3:
            a = str(y) + ' ** ' + str(w) + ' / ' + str(x) + ' ** ' + str(w)
            actual = y ** w / x ** w
            actual = round(actual, 2)
        # The fourth possible question
        elif z == 4:
            a = str(v) + ' ** ' + str(w) + ' - ' + str(x) + ' * ' + str(y)
            actual = v ** w - x * y
        # The final possible question
        elif z == 5:
            a = str(x) + ' / ' + str(y) + ' + ' + str(w) + ' ** ' + str(w)
            actual = x / y + w ** w
            actual = round(actual, 2)
        # This prints the problem and question for the user
        # The '+ 1' makes the problem number start on 1 not 0
        print("Problem " + str(i + 1))
        print(a)
        ans = input("What is the answer? ")
        # This checks the users answers and keeps score
        if float(ans) == actual:
            print("You got it!")
            correct += 1
        else:
            print("You missed that one...")
    # This calculates the users score and displays it
    percent_correct = correct/int(runtime) * 100
    print("You got %.02f percent right" % percent_correct)

# This section is for if the level input is invalid
else:
    print("You have selected Rainman difficulty")
    print("Make up your own math system.")


# This code will display a message to the user based on their score
if percent_correct >= 2 / 3 * 100:
    print("Well done!")
elif percent_correct >= 1 / 3 * 100 and percent_correct < 2 / 3 * 100:
    print("You need more practice...")
elif percent_correct < 1 / 3 * 100:
    print("Please ask your math teacher for help...")
