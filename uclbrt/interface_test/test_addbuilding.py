import requests
import json
import unittest


class MyTest(unittest.TestCase):  # 封装测试环境的初始化和还原的类
    def setUp(self):  # 放对数据可操作的代码，如对mysql、momgodb的初始化等,这里不对数据库进行操作！
        print("start test")
        pass

    def tearDown(self):  # 与setUp()相对
        print("end test")
        pass


class test_building_get(MyTest):  # 把这个接口封装一个类，下面的方法是具体的测试用例
    '''''接口名称：获取资质'''  # 这个描述接口名称


    def test_building_get(self):
        self.test_login_token_id()
        self.test_communtity_id()
        # '''''测试用例1：哈哈'''  # 这个描述接口用例名称
        # host = "115.29.142.212:8020"
        # link = "/Mobile/Room/addBuilding"
        # self.url = "http://" + host + link  # 请求url
        # print(self.url)
        # self.headers = {"Content-Type": "application/x-www-form-urlencoded"}
        # self.data = {  # 请求参数
        #     'id': ,
        #     # 'token':
        #       'token': ,
        #     'name': '2427',
        #     'num': '2',
        #     'contact': 'www',
        #     'areaCode': '86',
        #     'phone': '13480251015',
        #     'communityId': ,
        #     'desc': '',
        # }  # self.用在方法属性中，表示是该方法的属性，不会影响其他方法的属性。
        # print(json.dumps(self.data))
        # r = requests.post(url=self.url, data=self.data, headers=self.headers)
        # # return r.json()
        # print(r.text)
        # print()
        # self.assertIn("true", self.r.text)  # 断言判断接口返回是否符合要求，可以写多个断言！


if __name__ == "__main__":
    unittest.main()
