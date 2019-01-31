import fileController
import random

ip = str(random.randint(1, 20))

def test_ipCheker_create():
    assert fileController.ipChecker(ip) == None

    
def test_already_saved():
    assert fileController.ipChecker(ip) == False

def test_ipChecker_new():
    ip_new = str(random.randint(21, 40))
    assert fileController.ipChecker(ip_new) == True
