import os
import datetime
import random
from . import mkdir
#import datetime
now_time = datetime.datetime.now().strftime('%Y%m%d')
# 随机生成16位十六进制数字,生成文件名


path = os.path.dirname(os.path.realpath(__file__))+'/'+now_time

#
# def getRandomNum():
#     random_list = [i for i in range(0, 10)] + [chr(i) for i in range(97, 122)]
#     # 对应从“a”到“z”的ASCII码 [chr(i) for i in range(97,122)
#     random_str = ''
#     for i in range(16):
#         random_str = random_str + str(random_list[random.randint(1, 16)])
#     return random_str
#
# print(path)
# md = mkdir.MkDir()
# md.mkdir(path)

# with open(path+'/'+getRandomNum()+'.txt','w') as fb:
# 	fb.write('abc')



