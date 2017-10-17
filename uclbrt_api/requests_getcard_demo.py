#incoding=utf-8
import requests
import rsa
import urllib
accountSid = '1f739496ba56392b914fa5f3b9ad5fdd'
authToken = '9f52c2ab20db30e30a6ea6260771d9'
publicKkey = "-----BEGIN PUBLIC KEY-----MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAqxqOJg" \
             "0kqL4/xoNf0iDbjz/oM7ujsXOd92vQDkwO/rCP9wwZY0AvrMhcc56X4LmIbsbc1EZQ5ryMrIDbyCgtp" \
             "gJJTQG/u/FBiwG2Yvqgx+9keVGZhBA+Oph34HFPWz4OEB+Py4QkaJPXALkjjh2Zf7Lgpv5gO8gRyg/o9FwC" \
             "OZyEGiUmVorwPvwT3oMeNPCHxzlpGzdqV1kfqNmbS4ZkCiXGNhxxN0LJDnhaJJUl4bcnUjpcIxUlgSMX2" \
             "CcooffIk3E1ROP051Xf/zmUWE6DTcGetf6ni2s2irDCgeanylyjLTgM6xaOYWqtG0yUC5lyzO46yTmE1Q4" \
             "7XMM2h1KJswIDAQAB-----END PUBLIC KEY-----";
print publicKkey
info ="communityNo=1316880361&id=1f739496ba56392b914fa5f3b9ad5fdd&token=9f52c2ab20db30e30a6ea6260771d9&mobile=13480251015&areaCode=86&time=1508253409"
data = rsa.encrypt(info.encode(),publicKkey)
print data
url = 'http://cz.uclbrt.com/apiLogin/?data='+data
r = requests.get(url)
print r.text
