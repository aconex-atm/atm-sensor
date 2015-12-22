import RPi.GPIO as GPIO
import time
import monitor.http.sensorHttpService as httpService
from  monitor.http.sensorHttpService import Status

# GPIO setup
GPIO.setmode(GPIO.BCM)
TRIG = 23
ECHO =24
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
print ('setup distance measurment')


class Checker_ultrasonic:
    enabled=False
    toiletId=0
    currentStatus = Status.vacant;
    threshold = 0

    def __init__(self, tId, distance):
        self.enabled = True
        self.toiletId = tId
        self.currentStatus = Status.vacant
        self.threshold = 150

    def keepCheck(self):
        while(True):
                try:
                        dist = measure()
                        print (dist)
                        if dist<self.threshold:
                                print (dist ," cm")
                                if self.currentStatus ==  Status.vacant:
                                        httpService.setOccupied(self.toiletId)
                                        self.currentStatus = Status.occupied;
                        else:
                                if self.currentStatus == Status.occupied:
                                        httpService.setVacant(self.toiletId)
                                        self.currentStatus = Status.vacant;
                except (KeyboardInterrupt, SystemExit):
                        GPIO.cleanup()
        GPIO.cleanup()


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


