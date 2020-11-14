#!/usr/bin/python

from RPi import GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

left_sensor = 12
right_sensor = 7

GPIO.setup(left_sensor, GPIO.IN)
GPIO.setup(right_sensor, GPIO.IN)

try:
	while True:
		if not GPIO.input(left_sensor):
			print("Left Sensor")
		if not GPIO.input(right_sensor):
			print("Right Sensor")
		sleep(0.2)
except:
	GPIO.cleanup()
