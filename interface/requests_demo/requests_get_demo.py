import requests  
import  json  
payload = {'some': 'data'}  
headers = {'content-type': 'application/json'}  
r = requests.get('https://github.com/timeline.json', data=json.dumps(payload), headers=headers)  
print(r.json())