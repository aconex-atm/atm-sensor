import urllib.request

#http part
class Status:
	occupied = 'occupied'
	vacant='vacant'

def sendReq(status):
	url = "http://52.62.29.150:8080/ts/1/" + status
    req = urllib.request.Request(url, data=None, method='POST',   headers={'Content-Type': 'application/json'})
	resp = urllib.request.urlopen(req);
	print (status)

class sensorHttpService:
	def setOccupied():
    		sendReq(Status.occupied)

	def setVacant():
    		sendReq(Status.vacant)

def getDumpGoogle():
    url = "http://google.com.au"
    req = urllib.request.Request(url, data=None, method='GET')
    resp = urllib.request.urlopen(req);
    print (resp.read())
