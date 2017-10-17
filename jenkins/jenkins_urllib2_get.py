import urllib2
response = urllib2.urlopen('http://localhost:8080/api/json?pretty=true')
print response.read()