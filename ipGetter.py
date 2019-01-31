from requests import get
import fileController

def ipGetter():
    ip = get('https://api.ipify.org').text
    if ip:
        if fileController.ipChecker(ip):
                return ip
        