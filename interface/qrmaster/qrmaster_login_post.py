#incoding=utf-8
import requests
url='http://qrm.uclbrt.com/mobile/user/login'
data={'areaCode': '86', 'account': '18023496351','passwd': 't+wp6q7iDmh2/REdbSaHP7oYwf7B0h14uxQas6g/2MyRV7i8Lm15WgcOSVPAY7sRQn3lpdobaSvLXrqciL8H/4gG0TYGoRjziQi++ZzpiLfVPmLaJdXA6B7sXOOUcT6/N3XjDKZVFvohU3uMTOil6okJpjz88DfusPpjjzyjJgJAazI2cPfJ74xt80z6CebIGlRWrWRJnHO5bZ0EK6GrrMmLYycSfGfgMrpoeUyuoOnoQ6cMFBqoP6ewvjsRgUjdX2Yg6bKgMMyyqoSznjIUl3SXWp05U8D4VQDm0Cl63mXBmb/075YY82nnE8CuO/nW8MPeqXS5H9o0XRVBoVKTVg=='}
r = requests.post(url,data)
print r.text