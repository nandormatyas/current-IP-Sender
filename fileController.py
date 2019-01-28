import os.path

def ipChecker(ip):
    if os.path.exists("./ip.txt"):
        ipFile = open("ip.txt","r+")
        last_ip = ipFile.readlines()
        if last_ip[-1] == ip :
            ipFile.close()
            return False
        else : 
            ipFile.write("\n" + ip)
            ipFile.close()
            return True
    else :
        ipFile = open("ip.txt","w+")
        print('File created')
    
