import RPi.GPIO as GPIO
import time
import sensorHttpService
from  sensorHttpService import Status

# GPIO setup
GPIO.setmode(GPIO.BCM)
PIR_PIN = 7

GPIO.setup(PIR_PIN, GPIO.IN)
print ('setup IPR sensor')


# detecting function
def detect():
	print ('waiting for sensor to settle')
	time.sleep(2)
	print ("ready")

	while True:
		if GPIO.input(PIR_PIN):
			return True
		time.sleep(1)

#main app
currentStatus = Status.vacant;

while(True):
	try:
		detected = detect()
		if detected:
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


