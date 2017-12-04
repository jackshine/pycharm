#incoding=utf-8
import requests
r = requests.get('http://115.29.142.212:8010/Home/Public/login')
print r.text