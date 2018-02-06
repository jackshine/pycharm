# import datetime
# now_time = datetime.datetime.now().strftime('%Y%m%d')
# print(type(now_time))

import random


random_list = [i for i in  range(0,10)]+[chr(i) for i in range(97,122)]
#对应从“a”到“z”的ASCII码 [chr(i) for i in range(97,122)
list = ''
for i in range(16):
    list = list+str(random_list[random.randint(1, 16)])
