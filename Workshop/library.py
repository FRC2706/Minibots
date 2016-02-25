
# This is code for the Team 2706 Raspberry Pi worshop
# Building Block for participants to use

# CamJam EduKit 3 - Robotics
# Worksheet 9 – Obstacle Avoidance

import RPi.GPIO as GPIO # Import the GPIO Library
import time # Import the Time library


# Set the GPIO modes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set variables for the GPIO motor pins
pinMotorAForwards = 10
pinMotorABackwards = 9
pinMotorBBackwards = 8
pinMotorBForwards = 7

# Set variables for the GPIO ultrasound pins
pinTrigger = 26
pinEcho = 19

# How many times to turn the pin on and off each second
Frequency = 20
# How long the pin stays on each cycle, as a percent
DutyCycleA = 80
DutyCycleB = 80
# Settng the duty cycle to 0 means the motors will not turn
Stop = 0 # Set the GPIO Pin mode to be Output

GPIO.setup(pinMotorAForwards, GPIO.OUT)
GPIO.setup(pinMotorABackwards, GPIO.OUT)
GPIO.setup(pinMotorBForwards, GPIO.OUT)
GPIO.setup(pinMotorBBackwards, GPIO.OUT)
# Set pins as output and input
GPIO.setup(pinTrigger, GPIO.OUT)  # Trigger
GPIO.setup(pinEcho, GPIO.IN)      # Echo

# Set trigger to False (Low)
GPIO.output(pinTrigger, False)

# Allow module to settle
time.sleep(0.1)


# Set the GPIO to software PWM at 'Frequency' Hertz
pwmMotorAForwards = GPIO.PWM(pinMotorAForwards, Frequency)
pwmMotorABackwards = GPIO.PWM(pinMotorABackwards, Frequency)
pwmMotorBForwards = GPIO.PWM(pinMotorBForwards, Frequency)
pwmMotorBBackwards = GPIO.PWM(pinMotorBBackwards, Frequency)

# Start the software PWM with a duty cycle of 0 (i.e. not moving)
pwmMotorAForwards.start(Stop)
pwmMotorABackwards.start(Stop)
pwmMotorBForwards.start(Stop)
pwmMotorBBackwards.start(Stop)


def Forwards():
    pwmMotorAForwards.ChangeDutyCycle(DutyCycleA)
    pwmMotorABackwards.ChangeDutyCycle(Stop)
    pwmMotorBForwards.ChangeDutyCycle(DutyCycleB)
    pwmMotorBBackwards.ChangeDutyCycle(Stop)

# Turn both motors backwards
def Backwards():
    pwmMotorAForwards.ChangeDutyCycle(Stop)
    pwmMotorABackwards.ChangeDutyCycle(DutyCycleA)
    pwmMotorBForwards.ChangeDutyCycle(Stop)
    pwmMotorBBackwards.ChangeDutyCycle(DutyCycleB)

# Turn left
def Left():
    pwmMotorAForwards.ChangeDutyCycle(Stop)
    pwmMotorABackwards.ChangeDutyCycle(DutyCycleA)
    pwmMotorBForwards.ChangeDutyCycle(DutyCycleB)
    pwmMotorBBackwards.ChangeDutyCycle(Stop)

# Turn Right
def Right():
    pwmMotorAForwards.ChangeDutyCycle(DutyCycleA)
    pwmMotorABackwards.ChangeDutyCycle(Stop)
    pwmMotorBForwards.ChangeDutyCycle(Stop)
    pwmMotorBBackwards.ChangeDutyCycle(DutyCycleB)

def StopMotors():
    pwmMotorAForwards.ChangeDutyCycle(Stop)
    pwmMotorABackwards.ChangeDutyCycle(Stop)
    pwmMotorBForwards.ChangeDutyCycle(Stop)
    pwmMotorBBackwards.ChangeDutyCycle(Stop)



def drive(leftSpeed, rightSpeed, driveTime):
    '''A function to drive the motors at some speed for a set number of seconds.
    leftSpeed and rightSpeed should be float between -1 and 1'''
    if (leftSpeed > 0):
        pwmMotorAForwards.ChangeDutyCycle(leftSpeed * DutyCycleA)
        pwmMotorABackwards.ChangeDutyCycle(Stop)
    else:
        pwmMotorAForwards.ChangeDutyCycle(Stop)
        pwmMotorABackwards.ChangeDutyCycle(-leftSpeed * DutyCycleA)

    if (rightSpeed > 0):
        pwmMotorBForwards.ChangeDutyCycle(rightSpeed * DutyCycleB)
        pwmMotorBBackwards.ChangeDutyCycle(Stop)
    else:
        pwmMotorBForwards.ChangeDutyCycle(Stop)
        pwmMotorBBackwards.ChangeDutyCycle(-rightSpeed * DutyCycleB)


    time.sleep(driveTime)
    StopMotors()


def IsNearObstacle():
    Distance = getUltrasoundDist()

    print("IsNearObstacle: "+str(Distance))
    if Distance < 15:
        return True
    else:
        return False

def getUltrasoundDist():
    '''A function to fetch the distance from the ultrasound sensor.
    returns 'Units', no idea what the unit is'''

    # Send 10us pulse to trigger
    GPIO.output(pinTrigger, True)
    time.sleep(0.00001)
    GPIO.output(pinTrigger, False)

    # Start the timer
    StartTime = time.time()
    StopTime = StartTime

    # The start time is reset until the Echo pin is taken high (==1)
    while GPIO.input(pinEcho)==0:
        StartTime = time.time()
        StopTime = StartTime
    

    # Stop when the Echo pin is no longer high - the end time
    while GPIO.input(pinEcho)==1:
        StopTime = time.time()
        # If the sensor is too close to an object, the Pi cannot
        # see the echo quickly enough, so we have to detect that
        # problem and say what has happened.
        if StopTime-StartTime >= 0.04:
            print("Hold on there!  You're too close or far for me to see.")
            StopTime = StartTime
            break
        
    # Calculate travel time of the pulse
    ElapsedTime = StopTime - StartTime

    # Distance pulse travelled in that time is
    # time multiplied by the speed of sound (cm/s)
    Distance = ElapsedTime * 34326

    # That was the distance there and back so halve the value
    Distance = Distance / 2

    #print("Distance : %.1f" % Distance)
    time.sleep(0.25)

    return Distance
