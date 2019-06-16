from Adafruit_IO import MQTTClient
from src.services import adafruitService
import sys
import time

def initAction() :
    client = adafruitService.getInstanceMqttClient()
    
    client.on_connect    = connected
    client.on_disconnect = disconnected
    client.on_message    = message
    
    client.connect()
    client.loop_blocking()
    
def connected(client) :
    print('Connected to Adafruit IO!  Listening for feed changes...')
    client.subscribe('argos-feed.robotaction')

def disconnected(client) :
    print('Disconnected from Adafruit IO!')
    sys.exit(1)

def message(client, feed_id, payload) :
    print('Feed {0} received new value: {1}'.format(feed_id, payload))

    if feed_id == 'argos-feed.robotaction':
        switcher = {
            '10': right,
            '8': left,
            '5': straighOn,
            '13': backOff,
            '6': stop
        }
        try:
            func = switcher.get(payload)
            func()
        except TypeError:
            print("Invalid action")

def right() :
    print("right")
def left() :
    print("left")
def straighOn() :
    print("straigh On")
def backOff() :
    print("back off")
def stop() :
    print("stop")