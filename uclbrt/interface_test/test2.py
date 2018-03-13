import json
import requests


class A:


    def get_login_token_id(self):
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
            print(json.loads(self.r.text)['data']['token'])
            print(json.loads(self.r.text)['data']['id'])
            b = (json.loads(self.r.text)['data']['token'], json.loads(self.r.text)['data']['id'])
            return b


if __name__ == "__main__":
    a = A()
    a.get_login_token_id()
