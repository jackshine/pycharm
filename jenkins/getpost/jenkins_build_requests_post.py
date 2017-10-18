#encoding=utf-8
import requests
url = 'http://localhost:8080/job/check_python_version/enable'
r = requests.post(url,data={},auth=('admin','111111b'))
print r.text
