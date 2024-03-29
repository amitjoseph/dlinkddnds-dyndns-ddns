import urllib,json,socket,logging

# TO CHANGE --------------------
username="YOUR_USERNAME"
password="YOUR_PASSWORD"
domain="DOMAINNAME"
# ------------------------------

#Logging Configuration
logging.basicConfig(filename="/FULL_PATH_CHANGETHIS/ddns.log", format='%(asctime)s %(message)s',level=logging.DEBUG) 

def updateIp2Dyn(ip):
    updateURL="http://"+username+":"+password+"@members.dyndns.org/nic/update?hostname="+domain+"&myip="+ip+"&wildcard=NOCHG&mx=NOCHG&backmx=NOCHG"
    try:
        response =urllib.urlopen(updateURL)
        print response.read()
    except IOError:
            pass
    

#Get the public IP from ipify
def getPublicIP():
    publicIpURL="https://api.ipify.org?format=json"
    try:
        response =urllib.urlopen(publicIpURL)
        data=json.loads(response.read())
        ip=str(data['ip'])
        return ip
    except IOError:
       logging.critical('Cannot get Public IP!')
    
# Checks IP of the Domain and Public
# Updates new IP if it has changed
def checkDns():
    dnsIP=str(socket.gethostbyname(domain))
    publicIP=getPublicIP()
    
    if dnsIP == publicIP:
        logging.debug('Checked OK! '+dnsIP)
    else:
        updateIp2Dyn(publicIP)
        logging.critical("Updating IP "+publicIP)
        

def main():
    checkDns()

if __name__== "__main__":
  main()
