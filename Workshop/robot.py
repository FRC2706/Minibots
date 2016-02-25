# Raspberry Pi Robotics Worshop
# by FIRST Robotics Team 2706

import RPi.GPIO as GPIO # Import the GPIO Library
import time # Import the Time library
from library import *

pause = 5 # seconds

print("Starting in "+str(pause)+" seconds...")
time.sleep(pause) #Pause long enough for you to unplug cables
                  # and put it on the floor (15 seconds)
                  
# Type your code below here
#
#   Reminder
#       - drive(leftSpeed, rightSpeed, driveTime)
#       - IsNearObstacle()
#       - getUltrasoundDist()

