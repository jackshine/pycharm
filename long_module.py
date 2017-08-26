# coding=utf-8
from selenium import  webdriver
from selenium.webdriver.support.ui import WebDriverWait
url="http://115.29.142.212:8010/Home/BookPage/index.html"
login_text = '登录'
account = '13480251014'
pwd = '111111b'
def get_ele_time(driver,times,func):#得到一个元素在多少秒之内
    return WebDriverWait(driver,times).until(func)
def openBrower():
    '''
    return webdriver Handle
    '''
    webdriver_handle = webdriver.Firefox()
    return webdriver_handle
def openUrl(handle,url):
    handle.get(url)
    handle.maximize_window()

def findElement(d,arg):
    '''
    arg must dist
    1:text_id
    2:userid
    3:pwdid
    4:loginid
    return useEle,pwdEle,loginEle
    '''
    #if text_id in arg:
       # ele_login = get_ele_time(d,10,lambda d: d.find_element_by_link_text(arg['text_id']))
       #ele_login.click()
    useEle = d.find_element_by_id(arg['userid'])
    pwdEle = d.find_element_by_id(arg['pwdid'])
    loginEle = d.find_element_by_id(arg['loginid'])
    return (useEle,pwdEle,loginEle)
def sendVals(eletuple,arg):
    '''
    ele tuple
    acount :uname,pwd
    '''
    listkey = ['uname','pwd']
    i = 0
    for key in listkey:
        eletuple[i].send_keys('')
        eletuple[i].clear()
        eletuple[i].send_keys(arg[key])
        i+=1
    eletuple[2].click()

def login_test():
    d = openBrower()#打开浏览器
    openUrl(d,url)#打开链接
    ele_dict= {'text_id':'login_text','userid':'requestUsername',\
               'pwdid':'requestPassword','loginid':'requestSubmit'}
    ele_tuple = findElement(d,ele_dict)
    account_dict = {'uname':account,'pwd':pwd}
    sendVals(ele_tuple,account_dict)
    checkResult(d,"密码不正确")
def checkResult(d,text):
        text = d.find_element_by_id("login-tip").text
        print text
if __name__ == '__main__':
    login_test()



