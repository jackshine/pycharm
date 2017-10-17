import httplib

http_client = None
http_client = httplib.HTTPConnection('localhost',8080,timeout=30)
http_client.request('GET','/api/json?pretty=true')
response = http_client.getresponse()
print response.status