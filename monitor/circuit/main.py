import RPi.GPIO as GPIO
import time
import sensorHttpService
from  sensorHttpService import Status

# GPIO setup
GPIO.setmode(GPIO.BCM)
IN_PORT= 23
GPIO.setup(IN_PORT, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
print ('setup circuit checking')


#checking cirucuit 

#main app
currentStatus = Status.vacant;

while(True):
	try:
		if GPIO.input(IN_PORT) == 1:
			if currentStatus ==  Status.vacant:
				sensorHttpService.setOccupied()
				currentStatus = Status.occupied;
			else:
				pass
		else:
			if currentStatus == Status.occupied:
				sensorHttpService.setVacant()
				currentStatus = Status.vacant;
			else:
				pass
	except (KeyboardInterrupt, SystemExit):
		GPIO.cleanup()		

GPIO.cleanup()


