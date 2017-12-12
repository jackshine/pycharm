#coding:utf-8
def get_userinfo(path):
    user_info = {}
    config = open(path, encoding='utf-8')
    for line in config:
        result = line.split(';')
        for i in result:
            r = i.split('=')
            user_info[r[0]] = r[1]
    return user_info
if __name__== '__main__':
    info = get_userinfo('./userinfo.txt')
    print (info)