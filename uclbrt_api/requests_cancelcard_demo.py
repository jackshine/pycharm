#incoding=utf-8
import time
import hashlib
import base64
import urllib
import datetime
import requests
import json
accountSid = '1f739496ba56392b914fa5f3b9ad5fdd'
authToken = '9f52c2ab20db30e30a6ea6260771d9'
no = 'x20p3Vlnb6y5J8rO'
#得到body的形式为：{"no":"x20p3Vlnb6y5J8rO"}
body = {'no':no}
s =datetime.datetime.now() + datetime.timedelta(hours=-6)
batch = s.strftime("%Y%m%d%H%M%S")
sig =hashlib.md5(accountSid+authToken+batch).hexdigest().upper()
authen = base64.b64encode(accountSid+':'+batch)
header = {'Accept':'application/json','Content-Type':'application/x-www-form-urlencode;charset=uft-8','Authorization':authen}
url ='https://api.uclbrt.com:8058/?c=Qrcode&a=cancelCard&sig='+sig
r = requests.post(url,data=json.dumps(body),headers=header,verify=False)
print r.text
