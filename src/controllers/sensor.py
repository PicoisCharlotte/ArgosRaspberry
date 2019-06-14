from src.services import adafruitService
from Adafruit_IO import RequestError
import time

def initSensor() :
    while True :
        try :
            getValueSoundSensor()
            #setValueSoundSensor(10)
            getValueMotionSensor()
        except KeyboardInterrupt :
            break

#Sound sensor
def getValueSoundSensor() :
    aio = adafruitService.getInstanceAdafruitClient()
    try:
        soundSensor = aio.feeds('argos-feed.capteur-son')
    except RequestError:
        soundSensor = adafruitService.getCreateFeed(aio, 'argos-feed.capteur-son')

    data = aio.receive(soundSensor.key)
    time.sleep(2)
    print("Sound sensor value retrieve from Adafruit : " + data.value)

def setValueSoundSensor(value) :
    aio = adafruitService.getInstanceAdafruitClient()

    try:
        soundSensorFeed = aio.feeds('argos-feed.robotaction')
    except RequestError:
        soundSensorFeed = adafruitService.getCreateFeed(aio, 'argos-feed.robotaction')
    
    aio.send_data(soundSensorFeed.key, value)
    print("value post")
    time.sleep(5)

# Motion sensor
def getValueMotionSensor() :
    aio = adafruitService.getInstanceAdafruitClient()
    try:
        motionSensor = aio.feeds('argos-feed.capteur-mouvement')
    except RequestError:
        motionSensor = adafruitService.getCreateFeed(aio, 'argos-feed.capteur-mouvement')

    data = aio.receive(motionSensor.key)
    print("Motion sensor value retrieve from Adafruit : " + data.value)
    time.sleep(5)