import urllib,json

def UpdateIp2Dyn(ip):
    updateURL="http://USERNAME:PASSWORD@members.dyndns.org/nic/update?hostname=YOURDOMAIN.dlinkddns.com&myip="+ip+"&wildcard=NOCHG&mx=NOCHG&backmx=NOCHG"
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
        ip=data['ip']
        return ip
    except IOError:
        print 'No Internet!'
    
ip=str(getPublicIP())
UpdateIp2Dyn(ip)