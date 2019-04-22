#from cars import cars
import configparser

config = configparser.ConfigParser()
config.read('config/config.ini')

def main() :
    testVar = config['DEFAULT']['test']
    print(testVar)

main()
