# Name: theBackupPlan.py
# Purpose: control two motor from the command line either forward (clockwise)
#          or backwards (counterclockwise), left or right. Set distance
# Author: Darya Clark
# Date: 4 December 2022

#############################
#          SETUP            #
#############################

import RPi.GPIO as GPIO
from time import sleep

# set board to general pin input/output with BCM
GPIO.setmode(GPIO.BCM)
 
# set IN1, IN2, and ENA, respectively for motor1
in1 = 23
in2 = 24
enA = 25

# set IN3, IN4, and ENB respectively for motor2
in3 = 17
in4 = 27
enB = 22

# set motor outputs 
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(enA, GPIO.OUT)

GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)
GPIO.setup(enB, GPIO.OUT)

p1 = GPIO.PWM(enA,1000)
p1.start(25)

p2 = GPIO.PWM(enB,1000)
p2.start(25)

#############################
#    FUNCTION DEFINITIONS   #
#############################

# turn motors backwards for 3 seconds
def forward():
    # move forward motor 1
    p1.ChangeDutyCycle(50)
    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in2, GPIO.LOW)
    
    # move forward motor 2
    p2.ChangeDutyCycle(50)
    GPIO.output(in3, GPIO.HIGH)
    GPIO.output(in4, GPIO.LOW)
    sleep(1.5)

# turn motors backwards for 3 seconds
def backwards():
    # move backwards motor 1
    p1.ChangeDutyCycle(50)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)

    # move backwards motor 1
    p2.ChangeDutyCycle(50)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)

    sleep(1.5)


def rightTurn():
    # move forward motor 1
    p1.ChangeDutyCycle(50)
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.HIGH)
    # move backwards motor 2
    p2.ChangeDutyCycle(50)
    GPIO.output(in3, GPIO.HIGH)
    GPIO.output(in4, GPIO.LOW)
    
    sleep(1.5)

def leftTurn():
    # move backward motor 1
    p1.ChangeDutyCycle(50)
    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in2, GPIO.LOW)
    # move forward motor 2
    p2.ChangeDutyCycle(50)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.HIGH)
    
    sleep(1.5)

def stopMotors():
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)

    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.LOW)


#############################
#           main            #
#############################

print("\nWelcome to the Tank! The options for controls are f (forward), b (backwards), r (right turn), l (left turn), or q (quit)\n")


while True:
    # reset every loop
    stopMotors()
    # prompt user
    cmd = input("Command (f/b/q): ")
    if cmd == "f":
        forward()
    if cmd == "b":
        backwards()
    if cmd == "r":
        rightTurn()
    if cmd == "l":
        leftTurn()
    if cmd == "q":
        GPIO.cleanup()
        exit(0)
 






 