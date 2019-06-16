from Adafruit_IO import MQTTClient
from src.services import adafruitService
import sys
import time

def sendSensorValue() :
    client = adafruitService.getInstanceMqttClient()
    
    client.on_connect    = connected
    client.on_disconnect = disconnected
    
    client.connect()
    client.loop_background()
    time.sleep(5)
    while True :
        try :
            setIrSensor(client)
            setProximitySensor(client)
            setMotionSensor(client)
            setSoundSensor(client)
            time.sleep(5)
        except KeyboardInterrupt :
            break
    
def connected(client) :
    print('Connected to Adafruit IO!')

def disconnected(client) :
    print('Disconnected from Adafruit IO!')
    sys.exit(1)

def setIrSensor(client) :
    value = 10
    client.publish('argos-feed.capteur-ir', value)
    print("post")

def setProximitySensor(client) :
    value = 10
    client.publish('argos-feed.capteur-proximite', value)
    print("post")

def setMotionSensor(client) :
    value = 10
    client.publish('argos-feed.capteur-mouvement', value)
    print("post")

def setSoundSensor(client) :
    value = 10
    client.publish('argos-feed.capteur-son', value)
    print("post")