#encoding=utf-8
import os
from bs4 import BeautifulSoup
path = os.getcwd()
#用本地来创建对象
soup = BeautifulSoup(open(path+"/index.html"))
#print(soup.prettify())
print(soup.title.string)