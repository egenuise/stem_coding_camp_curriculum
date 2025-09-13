'''
This is the library that defines the Morse Code class
along with all of its functionality. Do not change the code here!
Otherwise your morse code project will not work properly.
'''

import time
import RPi.GPIO as GPIO

class MorseCode:

    def __init__(self, pin):
        self.pin = pin
        self._dotRest = .2

    def Speak(self, message):
        self.message = message
        message = message.upper()
        for i in range(0, len(message)):
            self._Translate(message[i])
            print(" ")
            time.sleep(self._dotRest)
        print("\n")

    def _Translate(self, letter):
        self.letter = letter
        if letter == "A":
            self._Dot()
            self._Dash()
        elif letter == "B":
            self._Dash()
            self._Dot()
            self._Dot()
            self._Dot()
        elif letter == "C":
            self._Dash()
            self._Dot()
            self._Dash()
            self._Dot()
        elif letter == "D":
            self._Dash()
            self._Dot()
            self._Dot()
        elif letter == "E":
            self._Dot()
        elif letter == "F":
            self._Dot()
            self._Dot()
            self._Dash()
            self._Dot()
        elif letter == "G":
            self._Dash()
            self._Dash()
            self._Dot()
        elif letter == "H":
            self._Dot()
            self._Dot()
            self._Dot()
            self._Dot()
        elif letter == "I":
            self._Dot()
            self._Dot()
        elif letter == "J":
            self._Dot()
            self._Dash()
            self._Dash()
            self._Dash()
        elif letter == "K":
            self._Dash()
            self._Dot()
            self._Dash()
        elif letter == "L":
            self._Dot()
            self._Dot()
            self._Dash()
            self._Dot()
        elif letter == "M":
            self._Dash()
            self._Dash()
        elif letter == "N":
            self._Dash()
            self._Dot()
        elif letter == "O":
            self._Dash()
            self._Dash()
            self._Dash()
        elif letter == "P":
            self._Dot()
            self._Dash()
            self._Dash()
            self._Dot()
        elif letter == "Q":
            self._Dash()
            self._Dash()
            self._Dot()
            self._Dash()
        elif letter == "R":
            self._Dot()
            self._Dash()
            self._Dot()
        elif letter == "S":
            self._Dot()
            self._Dot()
            self._Dot()
        elif letter == "T":
            self._Dash()
        elif letter == "U":
            self._Dot()
            self._Dot()
            self._Dash()
        elif letter == "V":
            self._Dot()
            self._Dot()
            self._Dot()
            self._Dash()
        elif letter == "W":
            self._Dot()
            self._Dash()
            self._Dash()
        elif letter == "X":
            self._Dash()
            self._Dot()
            self._Dot()
            self._Dash()
        elif letter == "Y":
            self._Dash()
            self._Dot()
            self._Dash()
            self._Dash()
        elif letter == "Z":
            self._Dash()
            self._Dash()
            self._Dot()
            self._Dot()
        elif letter == "1":
            self._Dot()
            self._Dash()
            self._Dash()
            self._Dash()
            self._Dash()
        elif letter == "2":
            self._Dot()
            self._Dot()
            self._Dash()
            self._Dash()
            self._Dash()
        elif letter == "3":
            self._Dot()
            self._Dot()
            self._Dot()
            self._Dash()
            self._Dash()
        elif letter == "4":
            self._Dot()
            self._Dot()
            self._Dot()
            self._Dot()
            self._Dash()
        elif letter == "5":
            self._Dot()
            self._Dot()
            self._Dot()
            self._Dot()
            self._Dot()
        elif letter == "6":
            self._Dash()
            self._Dot()
            self._Dot()
            self._Dot()
            self._Dot()
        elif letter == "7":
            self._Dash()
            self._Dash()
            self._Dot()
            self._Dot()
            self._Dot()
        elif letter == "8":
            self._Dash()
            self._Dash()
            self._Dash()
            self._Dot()
            self._Dot()
        elif letter == "9":
            self._Dash()
            self._Dash()
            self._Dash()
            self._Dash()
            self._Dot()
        elif letter == "0":
            self._Dash()
            self._Dash()
            self._Dash()
            self._Dash()
            self._Dash()
        else:
            time.sleep(self._dotRest)

    def _Dot(self):
        print(".")
        GPIO.output(self.pin, True)
        time.sleep(self._dotRest * 3/4)
        GPIO.output(self.pin, False)
        time.sleep(self._dotRest * 1/4)


    def _Dash(self):
        print("-")
        GPIO.output(self.pin, True)
        time.sleep(self._dotRest * 7/4)
        GPIO.output(self.pin, False)
        time.sleep(self._dotRest * 1/4)
        
    
