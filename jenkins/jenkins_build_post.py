#incoding=utf-8
import requests
url = 'http://localhost:8080/job/check_python_version/build'
r = requests.post(url , data={})
print r.text