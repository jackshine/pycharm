#!/usr/bin/python
import re
import urllib.request


def getHtml(url):
    print("aa")
    page = urllib.request.urlopen(url)
    html = page.read()
    return html


print(getHtml("https://www.douban.com/"))
