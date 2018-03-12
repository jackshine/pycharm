import redis

# conn = redis.Redis(host='localhost',port=6379,db=0)
# conn.set('k1','v1')
# val = conn.get('k1')
# print(val)

conn = redis.Redis(host='localhost',port=6379,db=1)

conn.lpush('names_list',*['把几个','鲁宁']) #
v = conn.llen('names_list')
#
for i in range(v):
    val = conn.rpop('names_list')
     #从右边第一条开始pop数据
    # val = conn.lpop('names_list')
     # 从左边第一条开始pop数据
    print(val.decode('utf-8'))
v = conn.llen('namessssss_list')
print(v)