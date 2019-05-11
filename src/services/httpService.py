import requests 

def getRequest(url, params) :
    r = requests.get(url = url, params = params)
    return r.json()