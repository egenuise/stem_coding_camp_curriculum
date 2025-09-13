import RPi.GPIO as GPIO


led = 23
button = 24
ledstate = False

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(button, GPIO.IN)

while True:
    if GPIO.input(button) and ledstate == False:
        GPIO.output(led, GPIO.HIGH)
        ledstate = True
    elif GPIO.input(button) and ledstate == True:
        GPIO.output(led, GPIO.LOW)
        ledstate = False

GPIO.cleanup()
