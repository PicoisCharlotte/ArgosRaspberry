from src.models import robot
from src.controllers import video, sensor
from config import globalVariable
import configparser

config = configparser.ConfigParser()
config.read('config/config.ini')
globalVariable.init(config)

def main() :
    #robot.getRobot(config)
    #video.getUrlVideo()
    sensor.initSensor()
main()
