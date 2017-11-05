#encoding=utf8
import requests
import unittest
url =  "http://127.0.0.1:16823/posts"
class test1(unittest.TestCase):
    def setUp(self):
        pass
    def test_aa(self,url):
        self.data = requests.get(url)
        print(self.data.text)
if __name__ == "__main__":
    a = test1()
    a.test_aa(url)