#incoding=utf-8
import requests
url = 'http://localhost:8080/api/json'
r = requests.get(url,params={'tree':'jobs[name,url]'},auth=('admin','111111b'))
print r.text