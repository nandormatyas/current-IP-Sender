from requests import get
import fileController

def ipGetter():
    ip = get('https://api.ipify.org').text
    #print('My public IP address is: {}'.format(ip))
    if fileController.ipChecker(ip) :
        return ip
    else :
      return False