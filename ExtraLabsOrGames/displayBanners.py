'''
Cruz Hernandez | Zach Messenger
cah587 | zam48
10/19/17
Lab Section 3
'''

# Dictionary which holds all letters in a 5x5 format
letters = {'a': {'a1': ' ### ',
                 'a2': '#   #',
                 'a3': '#####',
                 'a4': '#   #',
                 'a5': '#   #'},
           'b': {'b1': '#### ',
                 'b2': '#   #',
                 'b3': '#### ',
                 'b4': '#   #',
                 'b5': '#### '},
           'c': {'c1': '#####',
                 'c2': '#    ',
                 'c3': '#    ',
                 'c4': '#    ',
                 'c5': '#####'},
           'd': {'d1': '#### ',
                 'd2': '#   #',
                 'd3': '#   #',
                 'd4': '#   #',
                 'd5': '#### '},
           'e': {'e1': '#####',
                 'e2': '#    ',
                 'e3': '#####',
                 'e4': '#    ',
                 'e5': '#####'},
           'f': {'f1': '#####',
                 'f2': '#    ',
                 'f3': '#####',
                 'f4': '#    ',
                 'f5': '#    '},
           'g': {'g1': ' ### ',
                 'g2': '#    ',
                 'g3': '#  ##',
                 'g4': '#   #',
                 'g5': ' ### '},
           'h': {'h1': '#   #',
                 'h2': '#   #',
                 'h3': '#####',
                 'h4': '#   #',
                 'h5': '#   # '},
           'i': {'i1': '#####',
                 'i2': '  #  ',
                 'i3': '  #  ',
                 'i4': '  #  ',
                 'i5': '#####'},
           'j': {'j1': '#####',
                 'j2': '  #  ',
                 'j3': '  #  ',
                 'j4': '# #  ',
                 'j5': ' ##   '},
           'k': {'k1': '#   #',
                 'k2': '#  # ',
                 'k3': '##   ',
                 'k4': '#  # ',
                 'k5': '#   #'},
           'l': {'l1': '#    ',
                 'l2': '#    ',
                 'l3': '#    ',
                 'l4': '#    ',
                 'l5': '#####'},
           'm': {'m1': '#   #',
                 'm2': '## ##',
                 'm3': '# # # ',
                 'm4': '#   #',
                 'm5': '#   #'},
           'n': {'n1': '#   #',
                 'n2': '##  #',
                 'n3': '# # #',
                 'n4': '#  ##',
                 'n5': '#   #'},
           'o': {'o1': '#####',
                 'o2': '#   #',
                 'o3': '#   #',
                 'o4': '#   #',
                 'o5': '#####'},
           'p': {'p1': '#### ',
                 'p2': '#   #',
                 'p3': '#### ',
                 'p4': '#    ',
                 'p5': '#    '},
           'q': {'q1': '#### ',
                 'q2': '#  # ',
                 'q3': '#  # ',
                 'q4': '#### ',
                 'q5': '    #'},
           'r': {'r1': '#### ',
                 'r2': '#   #',
                 'r3': '#### ',
                 'r4': '#  # ',
                 'r5': '#   #'},
           's': {'s1': ' ### ',
                 's2': '##   ',
                 's3': '  #  ',
                 's4': '   ##',
                 's5': ' ### '},
           't': {'t1': '#####',
                 't2': '  #  ',
                 't3': '  #  ',
                 't4': '  #  ',
                 't5': '  #  '},
           'u': {'u1': '#   #',
                 'u2': '#   #',
                 'u3': '#   #',
                 'u4': '#   #',
                 'u5': ' ### '},
           'v': {'v1': '#   #',
                 'v2': '#   #',
                 'v3': ' # # ',
                 'v4': ' # # ',
                 'v5': '  #  '},
           'w': {'w1': '#   #',
                 'w2': '#   #',
                 'w3': '# # #',
                 'w4': '## ##',
                 'w5': '#   #'},
           'x': {'x1': '#   #',
                 'x2': ' # # ',
                 'x3': '  #  ',
                 'x4': ' # # ',
                 'x5': '#   #'},
           'y': {'y1': '#   #',
                 'y2': ' # # ',
                 'y3': '  #  ',
                 'y4': '  #  ',
                 'y5': '  #  '},
           'z': {'z1': '#####',
                 'z2': '   # ',
                 'z3': '  #  ',
                 'z4': ' #   ',
                 'z5': '#####'}}


# Banner Function
def print_banner(string, design):
    # Determines if banner will be vertical
    if design == 'vertical':
        # Accesses a single letter of a word
        for letter in string:
                # Gets each row of each letter
                for i in range(1, 6):
                    # Prints letters row by row
                    print(letters[letter][letter + str(i)])
                # Formats for same line
                print()
    # Determines if banner will be horizontal
    elif design == 'horizontal':
        # Gets all rows of letter
        for i in range(1, 6):
                # Gets letter
                for letter in string:
                    # Prints specific letter and next vertically
                    print(letters[letter][letter + str(i)], end=' ')
                # Puts space between each letter
                print()
    # Nice little error message
    else:
        print("You did something wrong...")


# Main Function
def main():
    # Gets desired word from the user
    string = input("Enter a word: ")
    # Gets desired orientation from the user
    design = input("Do you want your banner horizonatal or vertical: ").lower()
    # Calls banner function
    print_banner(string, design)

# Starts process
main()
