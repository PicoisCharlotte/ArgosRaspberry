from src.models import robot
import configparser

config = configparser.ConfigParser()
config.read('config/config.ini')

def main() :
    robot.getRobot(config)
main()
