from Adafruit_IO import Client, Feed
from config import globalVariable

def getInstanceAdafruitClient() :
    return Client(globalVariable.cfg['ADAFRUITIO']['USERNAME'], globalVariable.cfg['ADAFRUITIO']['KEY'])
def getCreateFeed(intstanceClient, feedName) :
    feed = Feed(name=feedName)
    return intstanceClient.create_feed(feed)

