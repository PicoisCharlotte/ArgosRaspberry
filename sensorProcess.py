from src.controllers import sensor
from config import globalVariable
import configparser

config = configparser.ConfigParser()
config.read('config/config.ini')
globalVariable.init(config)

def initProcessSensor() :
    sensor.initSensor()

initProcessSensor()