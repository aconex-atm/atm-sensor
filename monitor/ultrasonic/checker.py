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
    threshold_distance = 0
    threshold_time_occupy = 1
    threshold_time_vacant = 1
    def __init__(self, tId, distance = 150, time_occupy = 4, time_vacant = 2):
        self.enabled = True
        self.toiletId = tId
        self.currentStatus = Status.vacant
        self.threshold_distance = 150
        self.threshold_time_occupy = time_occupy
        self.threshold_time_vacant = time_vacant

    def keepCheck(self):
        time_enter_area = 0
        time_leave_area = 0
        while(True):
                try:
                        dist = measure()
                        if dist<self.threshold_distance:
                                print (dist ," cm")
                                if self.currentStatus ==  Status.vacant:
                                        if (time_enter_area <= self.threshold_time_occupy):
                                            time_enter_area +=1
                                            pass
                                        else:
                                            httpService.setOccupied(self.toiletId)
                                            self.currentStatus = Status.occupied;
                                            time_enter_area = 0
                        else:
                                if self.currentStatus == Status.occupied:
                                        if (time_leave_area <= self.threshold_time_vacant):
                                            time_leave_area +=1
                                        else:
                                            httpService.setVacant(self.toiletId)
                                            self.currentStatus = Status.vacant;
                                            time_leave_area = 0
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


