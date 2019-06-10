from src.services import adafruitService
from Adafruit_IO import RequestError
import time

def getValue() :
    aio = adafruitService.getInstanceAdafruitClient()
    try:
        sliderSon = aio.feeds('argos-feed.capteur-son')
    except RequestError:
        sliderSon = adafruitService.getCreateFeed(aio, 'argos-feed.capteur-son')

    while True:
        data = aio.receive(sliderSon.key)
        time.sleep(2)
        print(data.value)