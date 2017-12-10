import pickle
# d  =  dict(name='bob', age=20, score=88)
# f = open('dump.txt','wb')
# pickle.dump(d, f)
# 反序列化
f = open('./dump.txt','rb')
d = pickle.load(f)
f.close()
print(d)