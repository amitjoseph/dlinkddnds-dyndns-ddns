import urllib,json

# TO CHANGE --------------------
username="YOUR_USERNAME"
password="YOUR_PASSWORD"
domain="DOMAINNAME"
# ------------------------------

def updateIp2Dyn(ip):
    updateURL="http://"+username+":"+password+"@members.dyndns.org/nic/update?hostname="+domain+"&myip="+ip+"&wildcard=NOCHG&mx=NOCHG&backmx=NOCHG"
    try:
        response =urllib.urlopen(updateURL)
        print response.read()
    except IOError:
            pass
    


def getPublicIP():
    publicIpURL="https://api.ipify.org?format=json"
    try:
        response =urllib.urlopen(publicIpURL)
        data=json.loads(response.read())
        ip=str(data['ip'])
        return ip
    except IOError:
        print 'No Internet!'
    

def main():
    updateIp2Dyn(getPublicIP())

if __name__== "__main__":
  main()