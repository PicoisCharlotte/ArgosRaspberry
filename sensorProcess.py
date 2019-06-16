#from src.controllers.http import sensor
from src.controllers.mqtt import sensor
from config import globalVariable
import configparser

config = configparser.ConfigParser()
config.read('config/config.ini')
globalVariable.init(config)

def initProcessSensor() :
    sensor.sendSensorValue()

initProcessSensor()