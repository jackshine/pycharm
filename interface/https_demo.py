import urllib2
f = urllib2.urlopen("https://www.duba.com/?f=1&pid=&kptakeover")
buf = f.read()
print buf
f.close()
