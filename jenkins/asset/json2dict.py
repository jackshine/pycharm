#encoding=utf8
import json
d  = {"name":"lin","age":12}
print(json.dumps(d))
c = '{"name":"lin","age":12}'
print(json.loads(c))