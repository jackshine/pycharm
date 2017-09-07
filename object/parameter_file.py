#coding=utf-8
from selenium import webdriver
from  usedata_otherWay import getInfo,get_userinfo
import time
account_name = '13480251015'
account_pwd = "111111a"
list_Ele = []
def getHandler():
    return  webdriver.Firefox()
def openUrl(b,url):
    print  url
    b.get(url)
def findEle(b,dict):
    #找到元素
    print dict['name_id']
    name_Ele = b.find_element_by_id(dict['name_id'])
    pwd_Ele = b.find_element_by_id(dict['pwd_id'])
    login_Ele = b.find_element_by_id(dict['login_id'])
    list_Ele.append(name_Ele)
    list_Ele.append(pwd_Ele)
    list_Ele.append(login_Ele)
    print list_Ele
    return list_Ele
def sendInfo(list,arg):
    b = 0
    #查到到的元素句柄
    # name_Ele = b.find_element_by_id("requestUsername")
    # pwd_Ele = b.find_element_by_id("requestPassword")
    # login_Ele = b.find_element_by_id("requestSubmit")
    list_key = ['uname','pwd']
    print list
    b = 0
    for i in list_key:
        list[b].send_keys("")
        list[b].send_keys(arg[i])
        b+=1
    list[2].click()
#检查结果
def checkResult(b,text):
    try:
        a = b.find_element_by_id("login-tip").text
        print  a
        if b.find_element_by_id("login-tip").text==unicode(text,'utf-8'):
            print "error"
    except:
        print "Right"
def login_test(dict,user_list):
     #获得句柄
    b = getHandler()
    #打开浏览器
    openUrl(b,dict['url'])
    #查找元素，得到一个元组
    list = findEle(b,dict)
    #插入登录信息
    for i in user_list:
        sendInfo(list,i)
    #检查结果
    checkResult(b,dict['errorid'])
if __name__ == "__main__":
    print("aaa")
    dict = getInfo(r"D:\linyouwei\python\pycharm\object\webinfo.txt")
    print dict
    #user_list = [{'uname':account_name,'pwd':account_pwd}]
    userinfo = get_userinfo(r'D:\linyouwei\python\pycharm\object\userinfo.txt')
    login_test(dict,userinfo)