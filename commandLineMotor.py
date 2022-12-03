# Name: commandLineMotor.py
# Purpose: control a motor from the command line either forward (clockwise)
#          or backwards (counterclockwise)
# Author: Darya Clark
# Date: 3 December 2022

#############################
#          SETUP            #
#############################

import RPi.GPIO as GPIO
from time import sleep

# set board to general pin input/output 
GPIO.setmode(GPIO.BOARD)
 
# set IN1, IN2, and ENA, respectively
Motor1A = 16
Motor1B = 18
Motor1E = 22

# set motor outputs 
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)

#############################
#    FUNCTION DEFINITIONS   #
#############################

# turn motor clockwise for 3 seconds
def clockwise():
    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor1B,GPIO.LOW)
    GPIO.output(Motor1E,GPIO.HIGH)
    sleep(3)

# turn motor counterclockwise for 3 seconds
def counterClockwise():
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor1B,GPIO.HIGH)
    GPIO.output(Motor1E,GPIO.LOW)
    sleep(3)

# turn off outputs, then call reset to be able to continue program
def cleanUp():
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor1B,GPIO.LOW)
    GPIO.output(Motor1E,GPIO.LOW)
    GPIO.cleanup()
    reset()

# set up board 
def reset():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Motor1A,GPIO.OUT)
    GPIO.setup(Motor1B,GPIO.OUT)
    GPIO.setup(Motor1E,GPIO.OUT)


#############################
#           main            #
#############################

while True:
    # reset every loop
    cleanUp()
    # prompt user
    cmd = input("Command (f/b/q): ")
    if cmd == "f":
        clockwise()
    if cmd == "b":
        counterClockwise()
    if cmd == "q":
        GPIO.cleanup()
        exit(0)
 






 