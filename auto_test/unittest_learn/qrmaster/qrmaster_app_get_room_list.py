# encoding=utf-8
import requests
import unittest
import json
class TokenClass(unittest.TestCase):
    def setUp(self):
        pass
    def getToken(self):
        data = {"areaCode": "86", "account": "13480251015",
                "passwd":'''PoQwXiYLBjjNY6tjuWADi+HfsPqEpVqkR9MDy6MgWRvPMEdPBHrWXjJFmZvgDj3CQGPRiL04I5w1WGGmPd3fFty+sCIpw1A+K8DYnrMtCsxXjlKmO2VDBHbdZWbm32RdRdR4KnTrei+RQQRuZrjB6hhrnTN5/mjx51OlD/byhlL5SsBBU2C5x1MTvy/7PVN4EpxNFuYiNm/AQbp4Qfr5vK5bUhM+8Yr3AA7/uaEEklQO/pV51nv7hRYgs3y10WomZpoT8ygkgqwuirNVp/QikNPwWoCirXCIFpZE3zBBH2R8M4IjDwbwoaJpXRdptyFDzPaiAz7IonBLT7a3ZJDCew=='''}
        self.r = requests.post("http://qrm.uclbrt.com/mobile/user/login",data=data)
        dict = json.loads(self.r.text)
        print(dict)
        return(dict['data']['token'])

    def test_list(self):
        print(self.getToken())
        data = {"communityId":"641","id":"2664","token":self.getToken()}
        print(data)
        self.r = requests.post("http://qrm.uclbrt.com/Mobile/Room/item",data=data)
        print(self.r.text)
    def tearDown(self):
        pass
if __name__ == "__main__":
    sunit = unittest.TestLoader().loadTestsFromTestCase(TokenClass)
    unittest.TextTestRunner(verbosity=2).run(sunit)

