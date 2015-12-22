class CircuitChecker:
        enabled = False
        toiletId = 0

        def __init__(self, tId):
                self.toiletId = tId
        def setEnable (self, enable):
                self.enabled = enable
        def checkOnce (self):
                print ("i am checking")

