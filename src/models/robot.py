from src.services import httpService

def getRobot(config) :
    PARAMS = {'action': 'selectAllRobot'}
    test = httpService.getRequest(config['DEFAULT']['url'] + 'robot/select', PARAMS)
    print(test)