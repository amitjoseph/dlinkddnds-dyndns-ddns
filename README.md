# dlinkddnds-dyndns-ddns
 Update your [Dyanamic Ip](https://support.google.com/fiber/answer/3547208?hl=en) to your domain using Dydns / Dlinkddns Service.
### How to get a free DDNS Domain
If you own a dlink router/modem you're in luck, dlink provides one free ddns domain with each product. ( eg YOURNAME.dlinkddns.com )
visit dlinkddns.com for more information.
 ## Download the script using cURL
 ```
 curl -O https://raw.githubusercontent.com/amitjoseph/dlinkddnds-dyndns-ddns/master/code.py
 ```
 ### Make Changes

Edit the Username, Password and Domain name.
```
# TO CHANGE --------------------
username="YOUR_USERNAME"
password="YOUR_PASSWORD"
domain="DOMAINNAME"
# ------------------------------
....
```
## Schedule Script using Crontab
```
crontab -eu root
```
### Append this line to that file
```
*/5 * * * * python /filepath/code.py
```
This will run every 5 minutes. You can change the intervel accoording to your need.
