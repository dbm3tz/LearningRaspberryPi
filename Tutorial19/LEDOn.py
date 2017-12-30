# Raspberry Pi Tutorial 19 - GPIO Introduction with a(n) LED 

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

LEDPin = 22

GPIO.setup(LEDPin, GPIO.OUT)

try:
    while True:
        GPIO.output(LEDPin, True)
finally:
    # Reset the GPIO Pins to a safe state
    GPIO.cleanup()
