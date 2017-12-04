#incoding=utf-8
import httplib
import urllib
import requests
conn1 = httplib.HTTPConnection("http://115.29.142.212:8010")
reqheaders={'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',"Accept": "application/json, text/javascript, */*; q=0.01",
            "Host": "115.29.142.212:8010","Referer": "http://115.29.142.212:8010/login.html","User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

values = {"mobile":"13480251015","password":"111111b","areaCode":"86"}
data = urllib.urlencode(values)
conn1.request('POST','/Home/Public/login',data,reqheaders)
res=conn1.getresponse()
print res

