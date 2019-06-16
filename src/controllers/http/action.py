from src.services import adafruitService
from Adafruit_IO import RequestError
import time

def initAction() :
    robotMouvement()

def robotMouvement() :
    value = ''
    aio = adafruitService.getInstanceAdafruitClient()
    try:
        robotAction = aio.feeds('argos-feed.robotaction')
    except RequestError:
        robotAction = adafruitService.getCreateFeed(aio, 'argos-feed.robotaction')      
    while True :
        try :   
            data = aio.receive(robotAction.key)
            if value != data.value :
                value = data.value
                switcher = {
                    '10': right,
                    '8': left,
                    '5': straighOn,
                    '13': backOff,
                    '6': stop
                }
                try:
                    func = switcher.get(data.value)
                    func()
                except TypeError:
                    print("Invalid action")
            else :
                print('same')
                time.sleep(1)
        except KeyboardInterrupt :
            break

def right() :
    print("right")
    time.sleep(1)
def left() :
    print("left")
    time.sleep(1)
def straighOn() :
    print("straigh On")
    time.sleep(1)
def backOff() :
    print("back off")
    time.sleep(1)
def stop() :
    print("stop")
    time.sleep(1)
        

