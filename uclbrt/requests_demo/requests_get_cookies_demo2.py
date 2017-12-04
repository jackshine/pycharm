import requests

url = "http://115.29.142.212:8010/Home/Public/login"
data = {"areaCode":"86","mobile":"13480251015","password":"111111b"}
r = requests.get(url)
print(r.cookies['mz_UCLBRTUSSID'])