#incoding=utf-8
import urllib2
import urllib
url = 'http://115.29.142.212:8010/Home/Public/login'
values = {"mobile":"13480251015","password":"111111b","areaCode":"86"}
#对字典进行处理，得到以下形式
data = urllib.urlencode(values)
print data
req = urllib2.Request(url,data)
response = urllib2.urlopen(req)
info = response.read()
print info