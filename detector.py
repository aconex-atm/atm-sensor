import RPi.GPIO as GPIO
import time
import urllib.request

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




#http part
class Status:
	occupied = 'occupied'
	vacant='vacant'

def sendReq(status):
	url = "http://52.62.29.150:8080/ts/1/" + status
	req = urllib.request.Request(url, data=None, method='POST',   headers={'Content-Type': 'application/json'})
	resp = urllib.request.urlopen(req);

def setOccupied():
	sendReq(Status.occupied)

def setVacant():
	sendReq(Status.vacant)




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


