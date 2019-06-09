from src.models import robot
from src.controllers import video
import configparser

config = configparser.ConfigParser()
config.read('config/config.ini')

def main() :
    #robot.getRobot(config)
    video.getUrlVideo(config)
main()
