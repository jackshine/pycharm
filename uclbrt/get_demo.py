import urllib2
usl_s = 'http://www.baidu.com/'
info = urllib2.urlopen(usl_s).read()
print info