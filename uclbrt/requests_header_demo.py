#incoding=utf-8
import requests
import time
r = requests.post('http://115.29.142.212:8010/Home/Public/login',
                  data={"mobile":"13480251015","password":"111111b","areaCode":"86"})
print r.status_code