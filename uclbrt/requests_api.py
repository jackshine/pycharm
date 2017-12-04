#encoding=utf-8
import time
import hashlib
import base64
import urllib
import datetime
import requests
import json
accountSid = '1f739496ba56392b914fa5f3b9ad5fdd'
authToken = '9f52c2ab20db30e30a6ea6260771d9'
body = {'mobile':'13480251015','communityNo':'1316880361','buildNo':'001','floorNo':'001','roomNo':'001','startTime':'1710031000','endTime':'1710231000','areaCode':'86'}
s =datetime.datetime.now() + datetime.timedelta(hours=-6)
batch = s.strftime("%Y%m%d%H%M%S")
da = accountSid+authToken+batch
by = bytes(da,encoding="utf8")
hash_data = hashlib.md5(by)
sig =hash_data.hexdigest().upper()
print(sig)
authen = base64.b64encode(bytes(accountSid,encoding="utf8")+bytes("",encoding="utf8")+bytes(batch,encoding="utf8"))
print(str(authen))
header = {'Accept':'application/json','Content-Type':'application/x-www-form-urlencode;charset=uft-8','Authorization':authen}
url ='https://api.uclbrt.com:8058/?c=Qrcode&a=getLink&sig='+sig
#urllib.urlencode(body)
#url,body,header
#r = requests.post(url,json=body,headers=header,verify=False)
r = requests.post(url,data=json.dumps(body),headers=header,verify=False)
print(r.text)
