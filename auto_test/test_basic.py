account_name = '13480251015'
account_pwd = "111111b"
url = "http://115.29.142.212:8010/login.html"
list_key = ['account_name', 'account_pwd']
acount_list = {"account_name": account_name, "account_pwd": account_pwd, "url": url}
print(len(list_key))
for i in range(len(list_key)):
    print(acount_list[list_key[i]])
