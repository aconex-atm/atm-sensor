import RPi.GPIO as GPIO
import time
exec(open("sensorHttpService.py").read());

GPIO.setmode(GPIO.BCM)

TRIG = 23
ECHO =24

print ('setup distance measurment')

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def measure():
	GPIO.output(TRIG, False)
	# print 'waiting for sensor to settle'
	time.sleep(1)

	GPIO.output(TRIG, True)
	time.sleep(0.00001)
	GPIO.output(TRIG, False)

	while GPIO.input(ECHO)==0:
  		pulse_start = time.time();

	while GPIO.input(ECHO)==1:
  		pulse_end = time.time();

	pulse_duration = pulse_end - pulse_start

	distance = pulse_duration * 17150
	distance = round(distance, 2)
	return distance




#main app
currentStatus = Status.vacant;

while(True):
	try:
		dist = measure()
		if dist<150:
			print (dist ," cm")
			if currentStatus ==  Status.vacant:
				setOccupied()
			else:
				pass
		else:
			if currentStatus == Status.occupied:
				setVacant()
			else:
				pass
	except (KeyboardInterrupt, SystemExit):
		GPIO.cleanup()		

GPIO.cleanup()


