#encoding=utf8
import requests
import unittest
import  json
class test2(unittest.TestCase):
    def setUp(self):
        print("start")
    def tearDown(self):
        print("end")
    def test_aa(self):
        headers = {"content-type":"application/json"}
        json_data = json.dumps({"title":"new post","content":"new post"})
        r = requests.post("http://127.0.0.1:16823/posts",data=json_data,headers=headers)
        result = r.json()
        print(result)
        self.assertEquals(result['success'],'true')
if __name__ == "__main__":
    unittest.main()