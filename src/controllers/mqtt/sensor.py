from Adafruit_IO import MQTTClient
from src.services import adafruitService
import sys
import time
import serial

global ser
global value1
global value2
ser = serial.Serial('/dev/ttyACM0', 9600 )

def sendSensorValue() :
    client = adafruitService.getInstanceMqttClient()
    
    client.on_connect    = connected
    client.on_disconnect = disconnected
    
    client.connect()
    client.loop_background()
    time.sleep(5)
    while True :
        value1 = ser.readline().decode()
        print("valeur1 :")
        print(value1)
        value2 = ser.readline().decode()
        print("valeur2 :")
        print(value2)
        try :
            setMotionSensor(client, value2)
            setSoundSensor(client, value1)
            time.sleep(5)
        except KeyboardInterrupt :
            break
    
def connected(client) :
    print('Connected to Adafruit IO!')

def disconnected(client) :
    print('Disconnected from Adafruit IO!')
    sys.exit(1)

def setMotionSensor(client, value2) :
    client.publish('argos-feed.capteur-mouvement', value2)
    print("post")

def setSoundSensor(client, value1) :
    client.publish('argos-feed.capteur-son', value1)
    print("post")
