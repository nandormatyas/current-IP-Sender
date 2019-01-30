import os.path

def ipChecker(ip):
    if os.path.exists("./ip.txt"):
        ipFile = open("ip.txt","r+")
        last_ip = ipFile.readlines()
        if last_ip[-1] == ip:
            ipFile.close()
            return False
        else : 
            ipFile.write("\n" + ip)
            ipFile.close()
            return True
    else :
        ipFile = open("ip.txt","w+")
        ipFile.write(ip)
        print("ipFile created")
        ipFile.close()
    
def logCreator(time, message):
    if os.path.exists("./logs.txt"):
        logFile = open("logs.txt","r+")
        logFile.readlines()
        logFile.write("\n" + time + " " + message)
        logFile.close()
    else :
        logFile = open("logs.txt","w+")
        logFile.write(time + " " + message)
        print("logFile created")
        logFile.close()

