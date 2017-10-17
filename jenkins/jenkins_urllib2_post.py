#incoding=utf-8
import urllib2
import urllib
post_data = urllib.urlencode({})
url = 'http://localhost:8080/job/check_python_version/polling'
r = urllib2.urlopen(url,post_data)
print r.read()

