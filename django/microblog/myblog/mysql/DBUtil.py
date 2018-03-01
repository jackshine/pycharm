import pymysql as mdb


class DBUtil:
    __host = '127.0.0.1'
    __user = 'root'
    __passwd = ''
    __db = 'microblog'
    __port = 3306
    __charset = 'utf8'

    def __init__(self):
        self.host = DBUtil.__host
        self.user = DBUtil.__user
        self.passwd = DBUtil.__passwd
        self.db = DBUtil.__db
        self.port = DBUtil.__port
        self.conn = self.getConnection()

    def getConnection(self):
        conn = mdb.connect(host=self.host,
                           user=self.user,
                           passwd=self.passwd,
                           db=self.db,
                           port=self.port,
                           charset='utf8'
                           )
        return conn

    def execute(self, sql_str):
        if sql_str is None:
            raise Exception("参数不能为空：sql_str")
        if len(sql_str) == 0:
            raise Exception("参数不能为空：sql_str")
        try:
            conn = self.conn
            cur = conn.cursor()  # 获取一个游标
            cur.execute(sql_str)
            data = cur.fetchall()
            conn.commit()
            cur.close()  # 关闭游标
            conn.close()  # 释放数据库资源
            return data
        except Exception as e:
            raise e

    # 插入数据，返回数据主键
    def execute_insert(self, insert_str, data):
        if insert_str is None:
            raise Exception("参数不能为空：sql_str")
        if len(insert_str) == 0:
            raise Exception("参数不能为空：sql_str")
        try:
            conn = self.conn
            cur = conn.cursor()  # 获取一个游标
            cur.execute(insert_str, data)
            data = cur.fetchall()
            # last_id = cur.lastrowid
            last_id = conn.insert_id()
            conn.commit()
            cur.close()  # 关闭游标
            conn.close()  # 释放数据库资源
            return last_id
        except Exception as e:
            raise e

    # 更新数据，返回更新条数
    def execute_update(self, update_str, data):
        if update_str is None:
            raise Exception("参数不能为空：update_str")
        if len(update_str) == 0:
            raise Exception("参数不能为空：update_str")
        try:
            conn = self.conn
            cur = conn.cursor()  # 获取一个游标
            count = cur.execute(update_str, data)
            conn.commit()
            cur.close()  # 关闭游标
            conn.close()  # 释放数据库资源
            return count
        except Exception as e:
            raise e

    # 执行带参数的查询，返回查询结果
    def execute_select(self, select_str, data):
        if select_str is None:
            raise Exception("参数不能为空：sql_str")
        if len(select_str) == 0:
            raise Exception("参数不能为空：sql_str")
        try:
            conn = self.conn
            cur = conn.cursor()  # 获取一个游标
            cur.execute(select_str, data)
            data = cur.fetchall()
            conn.commit()
            cur.close()  # 关闭游标
            conn.close()  # 释放数据库资源
            return data
        except Exception as e:
            raise e

            # 执行带参数的查询，返回查询结果


    def execute_delete(self, select_str, data):
        if select_str is None:
            raise Exception("参数不能为空：sql_str")
        if len(select_str) == 0:
            raise Exception("参数不能为空：sql_str")
        try:
            conn = self.conn
            cur = conn.cursor()  # 获取一个游标
            cur.execute(select_str, data)
            data = cur.fetchall()
            conn.commit()
            cur.close()  # 关闭游标
            conn.close()  # 释放数据库资源
            return data
        except Exception as e:
            raise e


if __name__ == "__main__":
    # host, user, passwd, db, port, charset
    db = DBUtil()
    data = db.execute('SELECT * FROM userinfo')
