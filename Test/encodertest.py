import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(8,GPIO.IN)

while True:
	input = GPIO.input(8)
	if input:
		print ('1')
	else:
		print ('0')

