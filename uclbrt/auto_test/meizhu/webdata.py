#coding:utf-8
def get_webinfo(path):
    web_info = {}
    config = open(path, encoding='utf-8')
    for line in config:
        result = line.split('=')
        web_info[result[0]] = result[1].strip()
    return web_info
if __name__== '__main__':
    info = get_webinfo('./webinfo.txt')
    print (info)