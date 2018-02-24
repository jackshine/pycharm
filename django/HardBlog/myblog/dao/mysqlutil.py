import MySQLdb as mdb

# 连接数据库
conn = mdb.connect('localhost', 'root', '')

# 也可以使用关键字参数
conn = mdb.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='hardblog', charset='utf8')

# 也可以使用字典进行连接参数的管理
# config = {
#     'host': '127.0.0.1',
#     'port': 3306,
#     'user': 'root',
#     'passwd': '',
#     'db': 'blog',
#     'charset': 'utf8'
# }
# conn = mdb.connect(**config)

# 如果使用事务引擎，可以设置自动提交事务，或者在每次操作完成后手动提交事务conn.commit()
conn.autocommit(1)  # conn.autocommit(True)

# 使用cursor()方法获取操作游标
cursor = conn.cursor()
# 因该模块底层其实是调用CAPI的，所以，需要先得到当前指向数据库的指针。

try:
    # 创建数据库
    DB_NAME = 'hardblog'
    # cursor.execute('DROP DATABASE IF EXISTS %s' % DB_NAME)
    # conn.select_db(DB_NAME)
    TABLE_NAME = 'userinfo'
    cursor.execute('CREATE TABLE %S(USERID INT PRIMARY KEY,USERNAME VARCHAR(20),PASSWORD VARCHAR(32),REGTIME DATETIME,DELFLAG INT)' % TABLE_NAME)
    # count = cursor.execute('SELECT * FROM %S'%DB_NAME)
except:
    import traceback
    traceback.print_exc()
    # 发生错误时会滚
    conn.rollback()
finally:
    # 关闭游标连接
    cursor.close()
    # 关闭数据库连接
    conn.close()
