from requests import get


def ipGetter():
    ip = get('https://api.ipify.org').text
    #print('My public IP address is: {}'.format(ip))
    return ip