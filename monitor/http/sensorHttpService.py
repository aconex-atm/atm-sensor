import urllib.request
import urllib.parse

#http part
class Status:
	occupied = 'occupied'
	vacant='vacant'

base_url= "http://52.62.29.150:8080/level/4/room/1/male/slot/"

def sendReq(tid, status):
    emptyData = urllib.parse.urlencode({}).encode('utf8')
    url = base_url + str(tid) + "/" + status
    req = urllib.request.Request(url, data=emptyData,   headers={'Content-Type': 'application/json'})
    resp = urllib.request.urlopen(req);
    print ("sending http request :  ", url)

def setOccupied(tid):
  	sendReq(tid, Status.occupied)

def setVacant(tid):
   	sendReq(tid, Status.vacant)
