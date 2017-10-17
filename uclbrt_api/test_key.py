#incoding=utf-8
import rsa
# 生成密钥
(pubkey, privkey) = rsa.newkeys(1024)

# 明文
message =r"communityNo=1316880361&id=1f739496ba56392b914fa5f3b9ad5fdd&token=9f52c2ab20db30e30a6ea6260771d9&mobile=13480251015&areaCode=86&time=1508253409"

print pubkey
# 公钥加密
crypto = rsa.encrypt(message.encode(), pubkey)
print crypto


