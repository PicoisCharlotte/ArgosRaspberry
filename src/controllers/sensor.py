from src.services import adafruitService
from Adafruit_IO import RequestError
import time

def initSensor() :
    try:
        getValueSoundSensor()
        setValueSoundSensor(10)
    except KeyboardInterrupt:
        print("\nSound sensor process closed")

def getValueSoundSensor() :
    aio = adafruitService.getInstanceAdafruitClient()
    try:
        sliderSon = aio.feeds('argos-feed.capteur-son')
    except RequestError:
        sliderSon = adafruitService.getCreateFeed(aio, 'argos-feed.capteur-son')

    while True:
        data = aio.receive(sliderSon.key)
        time.sleep(2)
        print("Sound sensor value retrieve from Adafruit : " + data.value)

def setValueSoundSensor(value) :
    aio = adafruitService.getInstanceAdafruitClient()

    try:
        soundSensorFeed = aio.feeds('argos-feed.capteur-son')
    except RequestError:
        soundSensorFeed = adafruitService.getCreateFeed(aio, 'argos-feed.capteur-son')
    
    while True:
        aio.send_data(soundSensorFeed.key, value)
        print("value post")
        time.sleep(5)