'''
Zachary Messenger | John Wintroub
zam48 | jgw68
Lab section 3
10/26/2017
'''


# Import for the shuffle functionality
from random import shuffle

# List for holding High Scores
high_scores = []

# Dictionary that holds the questions
questions = [
            {'question': 'What was the name of the planet-destroying weapon?',
             'answers': ['Star Destroyer', 'Death Star', 'Executor',
                         'Death Ball'],
             'correct': '2'},
            {'question': 'Who shot first?',
             'answers': ['Han Solo', 'Greedo'],
             'correct': '1'},
            {'question': "Who is Luke Skwalker's father?",
             'answers': ['Jabba the Hutt', 'Yoda', 'Darth Vader',
                         'Obi-Wan Kenobi'],
             'correct': '3'},
            {'question': "What is the name of Han Solo's space ship?",
             'answers': ['Tantive IV', 'Devastator', 'Ghost',
                         'Millennium Falcon'],
             'correct': '4'},
            {'question': 'What is the name of the planet that Luke \
trains with Yoda on?',
             'answers': ['Dagobah', "Bespin", "Hoth"],
             'correct': '1'},
            {'question': 'What are the name of the aliens that live on Endor?',
             'answers': ['Wookiees', 'Trandoshans', 'Chiss', 'Ewoks'],
             'correct': '4'},
            {'question': 'What is the full name of the Emperor?',
             'answers': ['Darth Sidious', 'Darth Vader', 'Sheev Palpatine',
                         'Wilhuff Tarkin'],
             'correct': '3'},
            {'question': 'What is the name of the vehicle C-3P0 \
spots in the Dune Sea?',
             'answers': ['Dewback', 'Tantive IV', 'Troop Transport',
                         'Sand Crawler'],
             'correct': '4'},
            {'question': 'What is the name of the planet that is desroyed \
by the Empire?',
             'answers': ['Tatooine', 'Alderaan', 'Yavin IV', 'Dantooine'],
             'correct': '2'},
            {'question': 'What substance is Han Solo frozen in?',
             'answers': ['Carbonite', 'Red Matter', 'Vibranium'],
             'correct': '1'}
            ]
# This shuffles the questions for randomization every time
shuffle(questions)

# Intro statements that are printed to the user
print("Welcome to our Trivia Game")
print("The topic is Star Wars: episodes IV-VI")
print("How well do you know it?")
print()


# Game function
def game():
    print()
    # Score counter
    counter = 0
    # Question counter to print later and for score total
    question_number = 0
    # Accesses a single question
    for question in questions:
        # Adds one to the question counter for printing
        question_number += 1
        # Displays the question to the user
        print("Question " + str(question_number) + ". " + question["question"])
        for i, choice in enumerate(question["answers"]):
            # Prints the potential answers to the user
            print(str(i + 1) + ". " + choice)
        while True:
            # This is for if user enters an invalid option
            answer = input("Choose the number of your answer: ")
            # Checks the validity of the answer
            if int(answer) in range(len(question["answers"]) + 1):
                break
        # Evaluates if the answer is correct
        if answer == question['correct']:
            # Adds to the score
            counter += 1
            print('That is correct!')
            print("Current Score: " + str(counter) + " out of " +
                  str(question_number))
            print()
        else:
            # Does not add to score
            print("No")
            print("Current Score: " + str(counter) + " out of " +
                  str(question_number))
            print()
    print()
    return counter


# Game credits
def game_credits():
    # Contains our names
    print()
    print("This game is brought to you by:")
    print("Zach Messenger and John Wintroub")
    print()


# Function for viewing high scores
def view_high_score_table():
    print()
    # If scores in list then it will print
    if high_scores:
        print(high_scores)
    # If list is empty then will print message to the user
    else:
        print('High score table is empty. Sorry.')
        print("Play the game to add your score to the list.")
    print()


# Function for storing high scores
def storage(n):
    # For formatting
    if n < 10:
        n = '0' + str(n)
    else:
        n = str(n)
    # Get user identity
    name = input("Enter your initials: ")
    # Create high score name
    storage_name = n + '-' + name
    # Put score into list
    high_scores.append(storage_name)
    # Sort scores from lowest to highest
    high_scores.sort()
    # For deleting extra scores passed 10
    if len(high_scores) > 10:
        del high_scores[0]


# Main function with calls and main menu
def main():
    print("Main Menu")
    print()
    x = True
    while x:
        # Sees what the user wants to do
        user = int(input("Would you like 1. Play Game, \
2. View Credits, 3. Quit, or 4. View High Scores: "))
        if user == 3:
            print("Thank you for playing!")
            x = False
            continue
        elif user == 1:
            # Starts the game
            x = game()
            storage(x)
        elif user == 2:
            # Displays the credits
            game_credits()
        elif user == 4:
            # Shows high score table
            view_high_score_table()

main()
