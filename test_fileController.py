import fileController
import random

ip = str(random.randint(1, 20))

def test_ipCheker():
    assert fileController.ipChecker(ip) == True

def test_already_saved():
    assert fileController.ipChecker(ip) == False    
