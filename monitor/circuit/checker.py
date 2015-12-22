import RPi.GPIO as GPIO
import time
import sensorHttpService
from  sensorHttpService import Status

# GPIO setup
GPIO.setmode(GPIO.BCM)
IN_PORT= 23
GPIO.setup(IN_PORT, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

class CircuitChecker:
    enabled = False
    toiletId = 0

    def __init__(self, tId):
        self.toiletId = tId
        self.enabled = True
    def setEnable (self, enable):
        self.enabled = enable
        def checkOnce (self):
            if (not self.enabled):
                print ("The circuit checker for ", self.toiletId, "is disabled")
            else:
                return GPIO.input(IN_PORT) == 1
    def keepCheck(self):
        print ('setup circuit checking')
        if (not self.enabled):
            print ("The circuit checker for ", self.toiletId, "is disabled")
        else:
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

            
