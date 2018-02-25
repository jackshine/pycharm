import pymysql as mdb
import sys
# sys.path.append(r'D:\linyouwei\python\pycharm\django\microblog\myblog\mysql')
import DBUtil

class UserInfoDao:
    def __init__(self):
        self.db = DBUtil.DBUtil()

    def addUserInfo(self, username, password, regtime, delflag):
        # USERID INT PRIMARY KEY,USERNAME VARCHAR(20),PASSWORD VARCHAR(32),REGTIME DATETIME,DELFLAG INT
        self.db.execute_insert('insert into userinfo VALUE(userid,%s,%s,%s,%s)', (username, password, regtime, delflag))
    def getAllUserInfo(self):
        pass
    def getUserInfoById(self,id):
        data = self.db.execute_select("SELECT * FROM USERINFO WHERE userid=%s",id)
        return data
    def getUserInfoByName(self,name):
        data = self.db.execute_select("SELECT * FROM USERINFO WHERE username=%s",(name))
        print(data)
        dict = {}
        if data:
            data = data[0]
            dict['userid'] = data[0]
            dict['password'] = data[1]
            dict['regtime'] = data[2]
            dict['delflag'] = data[3]
        return dict
if __name__ == "__main__":
    db = UserInfoDao()
    db.addUserInfo('www','1111','2018-02-25 17:29:11','3')

