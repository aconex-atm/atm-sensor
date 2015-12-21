import urllib.request

# url = "http://localhost:3000"
# url = "http://52.62.29.150:8080/ts/1/vacant"
# req = urllib.request.Request(url, data=None, method='POST',   headers={'Content-Type': 'application/json'})
# resp = urllib.request.urlopen(req);
#
# the_page = resp.read()
# print (the_page)

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


# setVacant()
setOccupied()
