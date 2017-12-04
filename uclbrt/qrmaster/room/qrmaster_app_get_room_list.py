# encoding=utf-8
import requests
import unittest
import json
class TokenClass(unittest.TestCase):
    def setUp(self):
        pass
    def getToken(self):
        data = {"areaCode": "86", "account": "13480251015",
                "passwd":'''PmB63By77hCrBpaq0oAIS03BOMZu9dFahAV3hu+U4wpgl+YhlGUoCIPKJ9WZsQJYHmdJTe6yYdq+
        5Tg+lEEXXMyS6xPO+KRvuLadi84InZzBznmwN96NZ3eH3FC7kjKNYp2c5Sp57P06cCMdPgzRFu0+
        S1UK4IRb+WMiyqkSFzdo/UU4qnxIb66i3oqGoGdrA8z/AmWBOFybxwUjPTEe6Xz5ypxU7vvFtI2i
        szwd53vbMT/12nibrtpNhbr6hZYdxMY5M91u5XUPaV+ilMtUP2hFKEjnOm0Hzr3A6yxrxEBnjzEw
        bEnSq106LDyX6RH05dnmMw38eM7FrZeLePs/YQ=='''}
        self.r = requests.post("http://qrm.uclbrt.com/mobile/user/login",data=data)
        dict = json.loads(self.r.text)
        return(dict['data']['token'])

    def test_list(self):
        data = {"communityId":"641","id":"2664","token":self.getToken()}
        self.r = requests.post("http://qrm.uclbrt.com/Mobile/Room/item",data=data)
        print(self.r.text)
    def tearDown(self):
        pass
if __name__ == "__main__":
    sunit = unittest.TestLoader().loadTestsFromTestCase(TokenClass)
    unittest.TextTestRunner(verbosity=2).run(sunit)

