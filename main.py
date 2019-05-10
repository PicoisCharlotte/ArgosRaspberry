from src.http import http
import configparser

config = configparser.ConfigParser()
config.read('config/config.ini')

def main() :
    http.getRobot(config)
main()
