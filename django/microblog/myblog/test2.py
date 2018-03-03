import json
import datetime


class CJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S').replace("\"","")
        else:
            return json.JSONEncoder.default(self, obj)

now_time = datetime.datetime.now()
print(json.dumps(now_time, cls=CJsonEncoder))

print(json.dumps(now_time, cls=CJsonEncoder).replace("\"",""))