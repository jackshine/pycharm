# coding=utf-8
from selenium import webdriver
import time


class Login:
    def getHandler(self):
        return webdriver.Firefox()

    def openUrl(self,url):
        self.b.get(url)

    def findEle(self, ele_id_list):
        # 找到元素
        print(ele_id_list['mobile_id'])
        name_Ele =self.b.find_element_by_id(ele_id_list['mobile_id'])
        pwd_Ele = self.b.find_element_by_id(ele_id_list['pwd_id'])
        login_Ele = self.b.find_element_by_id(ele_id_list['login_id'])
        Ele_list = []
        Ele_list.append(name_Ele)
        Ele_list.append(pwd_Ele)
        Ele_list.append(login_Ele)
        return Ele_list

    def sendInfo(self,acount_list, Ele_list):
        list_key = ['account_name', 'account_pwd']
        for i in range(len(list_key)):
            Ele_list[i].send_keys("")
            Ele_list[i].send_keys(acount_list[list_key[i]])
        Ele_list[len(list_key)].click()

    def login_test(self, acount_list, ele_id_dict):
        self.b = self.getHandler()
        self.openUrl(acount_list['url'])
        Ele_list = self.findEle(ele_id_dict)
        self.sendInfo(acount_list, Ele_list)


if __name__ == "__main__":
    account_name = '13480251015'
    account_pwd = "111111b"
    url = "http://115.29.142.212:8010/login.html"
    acount_list = {"account_name": account_name, "account_pwd": account_pwd, "url": url}
    ele_id_dict = {"mobile_id": "requestUsername", "pwd_id": "requestPassword", "login_id": "requestSubmit"}
    login = Login()
    login.login_test(acount_list, ele_id_dict)
