import RPi.GPIO as GPIO
import time
import monitor.http.sensorHttpService as httpService
from  monitor.http.sensorHttpService import Status

# GPIO setup
GPIO.setmode(GPIO.BCM)
IN_PORT= 25
GPIO.setup(IN_PORT, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

class Checker_circuit:
    enabled = False
    toiletId = 0
    currentStatus = Status.vacant

    def __init__(self, tId):
        self.toiletId = tId
        self.enabled = True
        self.currentStatus = Status.vacant

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
            GPIO.add_event_detect(IN_PORT, GPIO.BOTH, callback=self.updateStatus)
            while 1:
                time.sleep(100)
    def updateStatus(self, *arg):
        if (not self.enabled):
            print ("The circuit checker for ", self.toiletId, "is disabled")
        if(GPIO.input(IN_PORT)):
            self.setStatusToOccupied()
        else:
            self.setStatusToVacant() 
 

    def setStatusToOccupied(self):
        if self.currentStatus == Status.vacant:
            httpService.setOccupied(self.toiletId)
            self.currentStatus = Status.occupied
        
    def setStatusToVacant(self): 
        if self.currentStatus == Status.occupied:
            httpService.setVacant(self.toiletId)
            self.currentStatus = Status.vacant;

