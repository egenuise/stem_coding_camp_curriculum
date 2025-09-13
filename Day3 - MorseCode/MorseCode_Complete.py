import MorseCodeLibrary
import RPi.GPIO as GPIO

MorseCode = MorseCodeLibrary.MorseCode

buzzer = 23

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer, GPIO.OUT)

Translator = MorseCode(buzzer)

while True:
    message = input("Enter your Morse Code Message: ")
    message = message.upper()
    print(message)
    Translator.Speak(message)
    
