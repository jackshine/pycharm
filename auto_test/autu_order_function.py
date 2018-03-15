# coding=utf-8
from selenium import webdriver
import time


def getHandler():
    return webdriver.Firefox()


def openUrl(b, url):
    b.get(url)


def findEle(b, ele_id_list):
    # 找到元素
    name_Ele = b.find_element_by_class_name("td-position")
    name_Ele.click()
    pwd_Ele = b.find_element_by_class_name(ele_id_list['pwd_id'])
    login_Ele = b.find_element_by_class_name(ele_id_list['login_id'])
    Ele_list = []
    Ele_list.append(name_Ele)
    Ele_list.append(pwd_Ele)
    Ele_list.append(login_Ele)

    return Ele_list


def sendInfo(acount_list, Ele_list):
    list_key = ['account_name', 'account_pwd']
    for i in range(len(list_key)):
        Ele_list[i].send_keys("")
        Ele_list[i].send_keys(acount_list[list_key[i]])
    Ele_list[len(list_key)].click()


def login_test(acount_list, ele_id_dict):
    b = getHandler()
    print(b)
    openUrl(b, acount_list['url'])
    Ele_list = findEle(b,ele_id_dict)
    # sendInfo(acount_list, Ele_list)

if __name__ == "__main__":
    url = "http://115.29.142.212:8010/Home/BookPage/index.html"
    acount_list = {"account_name": account_name, "account_pwd": account_pwd, "url": url}
    ele_id_dict = {"mobile_id": "requestUsername", "pwd_id": "requestPassword", "login_id": "requestSubmit"}
    login_test(acount_list, ele_id_dict)
