import requests 

def getRobot(config) :
    URL = config['DEFAULT']['url'] + 'robot/select'
    PARAMS = {'action': 'selectAllRobot'}
    r = requests.get(url = URL, params = PARAMS) 
    data = r.json() 
    print(data)