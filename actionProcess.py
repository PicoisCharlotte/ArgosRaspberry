from src.controllers import action
from config import globalVariable
import configparser

config = configparser.ConfigParser()
config.read('config/config.ini')
globalVariable.init(config)

def initProcessAction() :
    action.initAction()

initProcessAction()