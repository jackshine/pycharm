#encoding=utf-8
import rsa
import urllib
(pubKey,priKey) = rsa.newkeys(1024)
print(type(pubKey))
print(priKey)
message = 'linyouwei'
pubKey = rsa.PublicKey.load_pkcs1()
priKey = rsa.PrivateKey.load_pkcs1(priKey)
cryto = rsa.encrypt(message,pubKey)
priKey(cryto)

