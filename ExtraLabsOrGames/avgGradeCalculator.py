'''
    Lab 4 Grade Calculator
    rlb462 Rebecca Bohnker
    zam48 Zachary Messenger
    CS 126 Section 3
    10-05-2017
'''

# Grade Calculator

# This function is for average grade


def average(earned_score, max_score):
    # Sums each list and then determines average score
    x = sum(earned_score)
    y = sum(max_score)
    avg = x / y
    return avg

# This function will determine the letter grade for each portion of score


def letter_grade(percent):
    # Uses the return from the average function to determine letter grade
    if percent >= .9:
        return 'A'
    elif percent >= .8:
        return 'B'
    elif percent >= .7:
        return 'C'
    elif percent >= .6:
        return 'D'
    elif percent < .6:
        return 'F'

# This function calculates the portion of weighted grade from scores


def average_weighted(earned_score, max_score, weight):
    # Sums up lists to calculate average but then multiplies by the weight
    x = sum(earned_score)
    y = sum(max_score)
    avg = x / y
    weighted = avg * weight
    return weighted


# Main Function
# All values and functions are called from here


def main():
    # This portion is for determining the homework percentage and letter
    homework_score = [39, 40, 29, 40, 0, 5]
    max_homework = [40, 40, 40, 40, 40, 5]
    homework_grade = average(homework_score, max_homework)
    homework_letter = letter_grade(homework_grade)
    homework_weighted = average_weighted(homework_score, max_homework, .2)
    # Will print homework percentage and letter grade
    print("Homework Grade: " + str(round(homework_grade * 100)) + " (" +
          homework_letter + ") ")
    # This portion is for the quiz percentage and letter
    quiz_score = [10, 10, 9, 2, 10, 10, 10]
    quiz_max = [10, 10, 10, 10, 10, 10, 10]
    quiz_grade = average(quiz_score, quiz_max)
    quiz_letter = letter_grade(quiz_grade)
    quiz_weighted = average_weighted(quiz_score, quiz_max, .2)
    # Will print quiz percentage and letter grade
    print("Quiz Grade: " + str(round(quiz_grade * 100)) + " (" +
          quiz_letter + ") ")
    # This portion is for the test percentage and letter
    test_score = [293, 284, 300]
    test_max = [300, 300, 300]
    test_grade = average(test_score, test_max)
    test_letter = letter_grade(test_grade)
    test_weighted = average_weighted(test_score, test_max, .6)
    # Will print test percentage and letter grde
    print("Test Grade: " + str(round(test_grade * 100)) + " (" +
          test_letter + ") ")
    # This portion is for the overall percentage and letter
    score = test_weighted + quiz_weighted + homework_weighted
    score_letter = letter_grade(score)
    # Will print the final score and letter grade
    print("Final Score: " + str(round((score * 100))) + " (" + score_letter +
          ") ")

# Calls main and starts the whole process
main()
