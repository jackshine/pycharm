#encoding=utf-8
import requests
import unittest

class TokenClass(unittest.TestCase):
    def setUp(self):
        self.headers = {
            "Content-Type":"application/x-www-form-urlencoded",
        'User-Agent':'okhttp/3.8.0',
        }
    def getToken(self):
        data = {
            "areaCode":"86",
            "account":"13480251015",
            "passwd":'''YvruOVCimZrGK9hSC50gpmFvHImwZXYv6NNG81pKVo9FZSFLv+AYJHh6K1KiCq3/C3INkI3yjJ/7
PBAFQsGU6oHLewajs7wYkhALltn7WrlqovPx3x6XS6o2+bklvSkfCUUeoxbVLO7q+eyX8y4kAazF
gfpc+nDhXvLspDFixZPID/ccqW2NWCik4a1pdD0r1mr9R2k0FD5NxIOdVxyegs5W2E0ykIvsTfTG
24j7kT2NRhnO7ARNKAuYYXNCFAUPj4q8qlcKwlu3/S8S6oCHEf6G5AsZwDx4qoGX+eqJROS47AUP
co+KLBwEco/Y96xFLoOBhZqGwIp9y9/h848TyA=='''
        }
        self.r = requests.post("http://qrm.uclbrt.com/mobile/user/login",json=data,headers = self.headers)
        print(self.r)
