#encoding=utf-8
import requests
data = {"areaCode":"86","account":"13480251015",
        "passwd":'''PmB63By77hCrBpaq0oAIS03BOMZu9dFahAV3hu+U4wpgl+YhlGUoCIPKJ9WZsQJYHmdJTe6yYdq+
5Tg+lEEXXMyS6xPO+KRvuLadi84InZzBznmwN96NZ3eH3FC7kjKNYp2c5Sp57P06cCMdPgzRFu0+
S1UK4IRb+WMiyqkSFzdo/UU4qnxIb66i3oqGoGdrA8z/AmWBOFybxwUjPTEe6Xz5ypxU7vvFtI2i
szwd53vbMT/12nibrtpNhbr6hZYdxMY5M91u5XUPaV+ilMtUP2hFKEjnOm0Hzr3A6yxrxEBnjzEw
bEnSq106LDyX6RH05dnmMw38eM7FrZeLePs/YQ=='''}
print(data)
header = {'Accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencode;charset=uft-8'}
r = requests.post("http://qrm.uclbrt.com/mobile/user/login",data=data)
print(r.text)
