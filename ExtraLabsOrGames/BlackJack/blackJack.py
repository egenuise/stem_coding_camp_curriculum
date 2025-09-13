'''
Lab 12: Blackjack
Zachary Messenger | John Wintroub
zam48 | jgw68
Lab section 3
12-14-17
'''

# Imports random for shuffle, and classes from the previous lab
import random
from lab10_Answer_Key_MV import Card
from lab10_Answer_Key_MV import ChipBank
from random import shuffle


# Creation of the BlackjackHand class
class BlackjackHand():

    # Initiallization creates a list for each hand that gets registered
    def __init__(self):
        # List that stores the cards
        self.list = []

    # For adding a card to a hand
    def add_card(self, new_card):
        # Simple append to the list
        self.list.append(new_card)

    # For the printing of each hand
    def __str__(self):
        # List for assembly
        a = []
        # Loop through items in player or dealer hand
        for i in self.list:
            # Will append the card if faceup
            if i._facing_up:
                x = i.__str__()
                a.append(x)
            # Otherwise will say that particular card is facedown
            else:
                a.append("This card is facedown.")
        # Joins the items together in a neat statement and prints them
        return ','.join(a)

    # Gets the value of the player or dealer's hand
    def get_value(self):
        # Count to keep track of their value
        count = 0
        # Tracks the number of aces
        a = 0
        # Boolean value representing if the hand has an ace in it
        x = False
        # Loops through hand to check for aces first
        for i in self.list:
            # Checks if card is face up
            if i._facing_up:
                # Then checks for ace
                if i._rank == "Ace":
                    x = True
                    a += 1
                # If card is face down, moves to the next iteration
                else:
                    continue
        # Loops list to count values now
        for i in self.list:
            # If face up just adds
            if i._facing_up:
                count += i._value
            # If face down just goes to next iteration
            else:
                continue
        # Evaluates for aces if score is over 21
        if count > 21:
            # Checks if there is an ace
            if x is True:
                for i in range(0, a):
                    # Will turn an ace value into 1 if the player "Busts"
                    count -= 10
                    # If one iteration fixes then breaks loop
                    if count <= 21:
                        break
                    # Otherwise continues the loop
                    else:
                        continue
        # Returns the final count value
        return count

# Needed to create here or kept
player_hand = BlackjackHand()
dealer_hand = BlackjackHand()


# Creates the blackjack class for the actual playing of the game
class Blackjack():

    # Initialization occurs here for this class
    def __init__(self, starting_dollars):
        # Creates a list for storing of cards in the deck
        self.deck = []
        # Loops through 52 cards and card class to create a full deck
        for i in range(52):
            card = Card(i)
            self.deck.append(card)
        # Shuffles the deck
        shuffle(self.deck)
        # Creates a chipbank with the starting value
        self.balance = ChipBank(starting_dollars)
        # Creates a wager variable for keeping track of later
        self.wager = 0
        # For keeping track if a game is currently going
        self.game = 0

    # Draw function for drawing a card from adding to hand
    def draw(self):
        # Checks that deck has cards still
        if len(self.deck) != 0:
            # Takes the first card from the deck
            new_card = self.deck[0]
            # Cards should be drawn facing up
            new_card.face_up()
            # Deletes the first card from the deck
            self.deck = self.deck[1:]
        # If deck has no cards reshuffles it
        else:
            # Re-adds cards to the deck
            for i in range(52):
                card = Card(i)
                self.deck.append(card)
            # Shuffles
            shuffle(self.deck)
            # Takes first card
            new_card = self.deck[0]
            # Cards should be drawn faceup
            new_card.face_up()
            # Removes first card from deck
            self.deck = self.deck[1:]
        # Returns the card that was drawn
        return new_card

    # Function for starting a new game
    def start_hand(self, wager):
        # Shows that a game is now going
        self.game = 1
        # Adds first card for player
        player_hand.add_card(self.draw())
        # Dealers first card needs to be facedown
        x = self.draw()
        # x = x.face_down()
        dealer_hand.add_card(x)
        # Gives the player a second card
        player_hand.add_card(self.draw())
        # Gives the dealer a second card
        b = self.draw()
        dealer_hand.add_card(b)
        # Withdraws the wager amount from the chipbank
        x = self.balance.withdraw(wager)
        # Updates wager value that is kept track of
        self.wager = wager
        # Gets the value of the player and dealer hands
        c = str(player_hand.get_value())
        e = str(dealer_hand.get_value())
        # Should only see one dealer card
        d = str(b._value)
        # Displays the value to the user
        print("Player Hand: " + c)
        print("Dealer Hand: " + d + "...one is facedown...")
        # Checks for automatic game ends
        if c == "21" and e == "21":
            self.end_hand("Push")
        elif c == "21":
            self.end_hand("Win")
        elif e == "21":
            self.end_hand("Lose")

    # Function for player's turn
    def hit(self):
        # Will draw a card
        hit1 = self.draw()
        # Add card to the hand
        player_hand.list.append(hit1)
        # Prints the player's hand
        print(player_hand)
        # Prints the value of their hand
        print(player_hand.get_value())
        # If the 'busts' they lose
        if player_hand.get_value() > 21:
            self.end_hand("Lose")
        # If they get 21 they are forced to stand
        elif player_hand.get_value() == 21:
            self.stand()

    # Function for beginning the dealers turn
    def stand(self):
        # Turns all his cards face up
        for i in dealer_hand.list:
            i = i.face_up()
        # If dealer has a value of 16 or less, he must draw a card
        while dealer_hand.get_value() <= 16:
            dealer_hand.add_card(self.draw())
        # If dealer busts the player wins
        if dealer_hand.get_value() > 21:
            self.end_hand("Win")
        # If the dealer has the value of the player it's a push
        elif player_hand.get_value() == dealer_hand.get_value():
            self.end_hand("Push")
        # If the player is greater, the player wins
        elif player_hand.get_value() > dealer_hand.get_value():
            self.end_hand("Win")
        # If the dealer is greater the player loses
        elif player_hand.get_value() < dealer_hand.get_value():
            self.end_hand("Lose")

    # Presents the outcome of the game
    def end_hand(self, outcome):
        # For the player winning
        if outcome == "Win":
            # Prints both scores
            print("Dealer Hand: " + str(dealer_hand.get_value()))
            print("Player Hand: " + str(player_hand.get_value()))
            print("You win.")
            # Deposits twice the wager into players chipbank
            self.balance.deposit(2 * self.wager)
            # Clears both hands
            player_hand.list.clear()
            dealer_hand.list.clear()
        # For a tie
        elif outcome == "Push":
            # Prints both hands
            print("Dealer Hand: " + str(dealer_hand.get_value()))
            print("Player Hand: " + str(player_hand.get_value()))
            print("You tie.")
            # Deposits original wager back
            self.balance.deposit(self.wager)
            # Clears both hands
            player_hand.list.clear()
            dealer_hand.list.clear()
        # For the player Losing
        else:
            # Prints both hands
            print("Dealer Hand: " + str(dealer_hand.get_value()))
            print("Player Hand: " + str(player_hand.get_value()))
            print("You lose.")
            # Does not return wager or any money
            # Clears both hands
            player_hand.list.clear()
            dealer_hand.list.clear()
        # Resets the wager
        self.wager = 0
        # Sets the game to show no game is currently going
        self.game = 0

    # Checks to see if a game is active
    def game_active(self):
        # Uses prepared variable
        if self.game == 1:
            # Returns True if active
            return True
        else:
            # Returns False if not active
            return False

# The test code
if __name__ == "__main__":
    blackjack = Blackjack(250)
    while blackjack.balance.get_balance():
        print("Your remaining chips: "+str(blackjack.balance))
        wager = int(input("How much would you like to wager? "))
        blackjack.start_hand(wager)
        while blackjack.game_active():
            choice = input("STAND or HIT: ").upper()
            if choice == "STAND":
                blackjack.stand()
            elif choice == "HIT":
                blackjack.hit()
        print()
    print("Out of money! The casino wins!")
