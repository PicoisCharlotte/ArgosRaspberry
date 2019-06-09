import requests
import threading
import time

def getRequest(url, params) :
    r = requests.get(url = url, params = params)
    return r.json()

def sendUrl(url) :
    #t = threading.Timer(1.0, getUrl)
    #t.start()
   try:
       while True:
           print(url)
           time.sleep(2)
   except KeyboardInterrupt:
       print("\nkill program")