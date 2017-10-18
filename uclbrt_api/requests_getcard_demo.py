#encoding=utf-8
import requests
import rsa
import urllib
import base64
def getCard():
    accountSid = '1f739496ba56392b914fa5f3b9ad5fdd'
    authToken = '9f52c2ab20db30e30a6ea6260771d9'
    publicKkey = """-----BEGIN PUBLIC KEY-----
    MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAqxqOJg
    0kqL4/xoNf0iDbjz/oM7ujsXOd92vQDkwO/rCP9wwZY0AvrMhcc56X4LmIbsbc1EZQ5ryMrIDbyCgtp
    gJJTQG/u/FBiwG2Yvqgx+9keVGZhBA+Oph34HFPWz4OEB+Py4QkaJPXALkjjh2Zf7Lgpv5gO8gRyg/o9FwC
    OZyEGiUmVorwPvwT3oMeNPCHxzlpGzdqV1kfqNmbS4ZkCiXGNhxxN0LJDnhaJJUl4bcnUjpcIxUlgSMX2
    CcooffIk3E1ROP051Xf/zmUWE6DTcGetf6ni2s2irDCgeanylyjLTgM6xaOYWqtG0yUC5lyzO46yTmE1Q4
    7XMM2h1KJswIDAQAB
    -----END PUBLIC KEY-----"""
    publicKkey = rsa.PublicKey.load_pkcs1_openssl_pem(publicKkey)
    info ="communityNo=1316880361&id=1f739496ba56392b914fa5f3b9ad5fdd&token=9f52c2ab20db30e30a6ea6260771d9&mobile=18926368199&areaCode=86&time=1508323844"
    data = rsa.encrypt(info, publicKkey)
    url = 'http://cz.uclbrt.com/apiLogin/?data='+urllib.quote_plus(base64.b64encode(data))
    print(url)
if __name__ == "__main__":
    getCard()