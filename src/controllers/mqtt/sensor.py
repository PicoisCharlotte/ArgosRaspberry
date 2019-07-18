from Adafruit_IO import MQTTClient
from src.services import adafruitService
import sys
import time
import serial

global ser
global value1
global value2
countMotion = 0
countSound = 0
debug = False
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
        if debug: print("value 1 : ", value1)
        value2 = ser.readline().decode()
        if debug: print("value 2 : ", value2)
        try :
            setMotionSensor(client, value2)
            setSoundSensor(client, value1)
            time.sleep(2)
        except KeyboardInterrupt :
            break
    
def connected(client) :
    print('Connected to Adafruit IO!')

def disconnected(client) :
    print('Disconnected from Adafruit IO!')
    sys.exit(1)

def setMotionSensor(client, value2) :
    if int(value2) == 1 :
        if debug: print("countMotion : ", countMotion) 
        if countMotion <= 1 :
            client.publish('argos-feed.capteur-mouvement', value2)
            if debug: print("post")
        incrementMotion()
    elif(int(value2) == 0) :
        decrementMotion()

def setSoundSensor(client, value1) :
    if int(value1) == 1 :
        if debug: print("countSound : ", countSound)
        if countSound <= 1 :
            client.publish('argos-feed.capteur-son', value1)
            if debug: print("post")
        incrementSound()
    elif(int(value1) == 0) :
        decrementSound()
def incrementMotion() :
    global countMotion
    countMotion = countMotion + 1
def decrementMotion() :
    global countMotion
    countMotion = 0
def incrementSound() :
    global countSound
    countSound = countSound + 1
def decrementSound() :
    global countSound
    countSound = 0
    