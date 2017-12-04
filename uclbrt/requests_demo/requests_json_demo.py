#encoding=utf-8
import requests
r = requests.get("https://github.com/timeline.json")
print(type(r.json()))