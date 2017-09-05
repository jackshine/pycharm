#coding:utf-8
def get_webinfo(path):
    web_info = {}
    config = open(path)
    for line in config:
        result = line.split('=')
        web_info.update(dict([result]))
        print (result)
    return web_info
if __name__== '__main__':
    info = get_webinfo(r'D:\linyouwei\python\pycharm\object\webinfo.txt')
    print  info