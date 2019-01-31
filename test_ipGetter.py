import ipGetter
import random
from requests import get

ip = str(random.randint(1, 20))

def test_on_change():
    assert ipGetter.ipGetter() == get('https://api.ipify.org').text
    
def test_no_change():
    assert ipGetter.ipGetter() == None