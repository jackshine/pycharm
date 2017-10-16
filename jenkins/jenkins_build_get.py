#incoding=utf-8
import requests
url = 'http://localhost:8080/api/json?pretty=true'
r = requests.get(url,params={},auth=('admin','111111b'))
print r.text