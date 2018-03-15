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
    @staticmethod
    def test_login_token_id(self):
        host = "115.29.142.212:8020"
        link = "/mobile/user/login"
        self.url = "http://" + host + link  # 请求url
        self.data = {  # 请求参数
            'areaCode': '86',
            'account': '13480251015',
            'l': 'zh_cn',
            'passwd': 'J4oXyCwYfNiOD5FlhqL3agZRTP6Futhcsi52Rf+7mYPfo6Lb90xfdEnC/6OBsSqQ5y9b67YzEFPNaaK+p+KgeuNwmkjMkT0Zv61nUbS2YgNUk89DUALv8s0BYS3dnHEwLuy3In2vtOXCYdurgyT0CZWvX+glsKcMochghDAduuaP6dabFWSroPC1ZPuKl6k8YWr+8OVZyTW2NHiUzY9+KFo7NmUAvUagutit6iUzfwONAoA5JNIkb5Lz6mn2TWEriERdJb7pa6TSSsDBik40rw5IB0B+hSZChmlJKBdAwPXwQq2qGFyQQsu80hWvWCkWnx5jGLABqCI4qiHZ0EthLQ==',
        }  # self.用在方法属性中，表示是该方法的属性，不会影响其他方法的属性。
        self.r = requests.post(url=self.url, data=self.data)
        if json.loads(self.r.text)['status'] == 200:
            # print(json.loads(self.r.text)['data']['token'])
            # print(json.loads(self.r.text)['data']['id'])
            b = (json.loads(self.r.text)['data']['token'], json.loads(self.r.text)['data']['id'])
            return b

    def test_communtity_id(self):
        host = "115.29.142.212:8020"
        link = "/mobile/Community/getCommunitiesWithAuthority"
        self.url = "http://" + host + link  # 请求url
        print(self.test_login_token_id())
        self.data = {  # 请求参数
            'id': self.test_login_token_id()[1],
            'l': 'zh_cn',
            'token': self.test_login_token_id()[0]
        }  # self.用在方法属性中，表示是该方法的属性，不会影响其他方法的属性。
        self.r = requests.post(url=self.url, data=self.data)
        print(self.r.text)
        if json.loads(self.r.text)['status'] == 200:
            # print(json.loads(self.r.text)['communities']['communityid'])
            return json.loads(self.r.text)['communities']['communityid']

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
