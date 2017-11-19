#encoding=utf-8
import re
str = '/Bpass/ComAuthority/companyStatus/id/581/userloginID/1623.html'
reObj1 = re.compile('[0-9]+')
print(reObj1.findall(str))
