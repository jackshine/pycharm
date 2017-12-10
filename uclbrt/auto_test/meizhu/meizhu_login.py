# coding=utf-8
import unittest
from openpyxl import load_workbook
import requests
class Test(unittest.TestCase):
    def setUp(self):
        self.meizhu_client = 'http://115.29.142.212:8010'
        print('start')
    def test_case1(self):
        # 读取账号
        rb = load_workbook(filename='./meizhu_account.xlsx')
        table = rb.get_sheet_by_name("Sheet1")
        mobile = str(int(table.cell(1,0).value))
        password = table.cell(1,1).value
        areaCode = str(int(table.cell(1,2).value))
        data = {
            'mobile':mobile,
            'password':password,
            'areaCode':areaCode
        }
        print(data)
        # 请求网络 # http://115.29.142.212:8010/Home/Public/login
        resp = requests.post(self.meizhu_client+'/Home/Public/login',data=data)
        print(resp.text)
        # 根据网络返回的状态判断是否成功
        self.assertEqual(resp.status_code, 200, msg='success')
        # 将结果写入excel
        table.cell(row=2, column=4).value =str(resp.status_code)
        rb.save('./meizhu_account.xlsx')

    def tearDown(self):
        print("end")
if __name__ == "__main__":
    unittest.main









