#coding=utf-8
from selenium import webdriver
import time
url = "http://115.29.142.212:8010/Home/BookPage/index.html"
account_name = '13480251015'
accout_pwd = "111111a"
list_Ele = []
def getHandler():
    return  webdriver.Firefox()
def openUrl(b,url):
    b.get(url)
def findEle(b,dict):
    #找到元素
    name_Ele = b.find_element_by_id(dict['name_id'])
    pwd_Ele = b.find_element_by_id(dict['pwd_id'])
    login_Ele = b.find_element_by_id(dict['login_id'])
    list_Ele.append(name_Ele,pwd_Ele,login_Ele)
    return list_Ele

def sendInfo(account,list):
    #list   [name_Ele,pwd_Ele,login_Ele]
    #list_key = ['name','pwd']
    b = 0
    list_key = ['name','pwd']
    for t in list:
        t[b].send_keys("")
        t[b].clear()
        t[b].send_keys(account[list_key[b]])
        b+1
        if(b==2):
            t[b].click()
#检查结果
def login_test():
     #获得句柄
    b = getHandler()
    #打开浏览器
    openUrl(b,url)
    #查找元素，得到一个元组
    dict = {'name_id':"requestUsername","pwd_id":"requestPassword","login_id":"requestSubmit"}
    list = findEle(b,dict)
    print tuple
    #插入登录信息
    account = {"name":account_name,"pwd":accout_pwd}
    sendInfo(account,list)
if __name__ == "main":
    login_test()