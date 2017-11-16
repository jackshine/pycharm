#encoding=utf-8
import requests
import time
login_url = 'http://115.29.142.212:8020/Home/Public/login'
url ="http://115.29.142.212:8020/login.html"
s = requests.session()
r = s.get(url)
print(r.cookies)
data ={
        "mobile":"13480251015",
        "areaCode":"86",
        "password":"bbc69d27003568a7a94626ce4337bc9d",
        "hash":"5c3d9515c82390c5c66b306598b6b276"
}
time.sleep(1)
a = s.post(login_url,data=data)
print(a.text)