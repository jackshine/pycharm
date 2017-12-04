import requests

url = "http://httpbin.org/post"
files = {'file':open("report.txt",'rb')}
r = requests.post(url,files=files)
print(r.headers)
