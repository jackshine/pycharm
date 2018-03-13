import requests
import json
import unittest
import time
from HTMLTestRunner import HTMLTestRunner

class MyTest(unittest.TestCase):  # 封装测试环境的初始化和还原的类
    def setUp(self):  # 放对数据可操作的代码，如对mysql、momgodb的初始化等,这里不对数据库进行操作！
        print("start test")
        pass

    def tearDown(self):  # 与setUp()相对
        print("end test")
        pass


class test_login_get(MyTest):  # 把这个接口封装一个类，下面的方法是具体的测试用例
    '''''接口名称：获取资质'''  # 这个描述接口名称

    def test_login_get(self):
        '''''测试用例1：哈哈'''  # 这个描述接口用例名称
        host = "115.29.142.212:8020"
        link = "/mobile/user/login"
        self.url = "http://"+host+link  # 请求url
        print(self.url)
        self.headers = {"Content-Type": "application/x-www-form-urlencoded"}
        self.data = {  # 请求参数
            'areaCode':'86',
            'account': '13480251015',
            'l': 'zh_cn',
            'passwd': 'J4oXyCwYfNiOD5FlhqL3agZRTP6Futhcsi52Rf+7mYPfo6Lb90xfdEnC/6OBsSqQ5y9b67YzEFPNaaK+p+KgeuNwmkjMkT0Zv61nUbS2YgNUk89DUALv8s0BYS3dnHEwLuy3In2vtOXCYdurgyT0CZWvX+glsKcMochghDAduuaP6dabFWSroPC1ZPuKl6k8YWr+8OVZyTW2NHiUzY9+KFo7NmUAvUagutit6iUzfwONAoA5JNIkb5Lz6mn2TWEriERdJb7pa6TSSsDBik40rw5IB0B+hSZChmlJKBdAwPXwQq2qGFyQQsu80hWvWCkWnx5jGLABqCI4qiHZ0EthLQ==',
        }  # self.用在方法属性中，表示是该方法的属性，不会影响其他方法的属性。
        print(json.dumps(self.data))
        r = requests.post(url=self.url, data=self.data)
        # return r.json()
        status = json.loads(r.text)['status']
        print(type(status))
        self.assertEqual(200,status)  # 断言判断接口返回是否符合要求，可以写多个断言！


if __name__ == "__main__":
    # suite = unittest.TestSuite()
    # suite.addTest(test_login_get.test_login_get("test_login_get"))
    # testunit = unittest.TestSuite()
    # testunit.addTest(suite)
    suite = unittest.makeSuite(test_login_get)
    # # 按照一定的格式获取当前的时间
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    test_report = r"D:\linyouwei\python\pycharm\uclbrt\interface_test"
    # 定义报告存放路径
    filename = test_report + "\\" + now + 'result.html'
    print(filename)
    fp = open(filename, "wb")

    # 定义测试报告
    runner = HTMLTestRunner(stream=fp,
                            title="接口测试报告",
                            description="测试用例执行情况：")

    # 运行测试
    runner.run(suite)
    fp.close()  # 关闭文件对象把数据写进磁盘
    print('aaa')
