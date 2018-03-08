import pymysql as mdb
import sys
sys.path.append(r'D:\linyouwei\python\pycharm\django\microblog\myblog\mysql')
import DBUtil

class UserInfoDao:
    def __init__(self):
        self.db = DBUtil.DBUtil()
    def addUserInfo(self,username,password,create_time):
        #USERID INT PRIMARY KEY,USERNAME VARCHAR(20),PASSWORD VARCHAR(32),REGTIME DATETIME,DELFLAG INT
        db =DBUtil.DBUtil()
        db.execute_insert('insert into user_login VALUE(id,%s,%s,%s)',(username,password,create_time))
    def getAllUserInfo(self):
      pass

    def searchUserInfo(self,str):
        db = DBUtil()
        dataList = db.execute("select * from user_login where username like '%"+str+"%'")
        dict = {}
        userList = []
        for row in dataList:
            dict['id'] = row[0]
            dict['username'] = row[1]
            dict['password'] = row[2]
            dict['create_time'] = json.dumps(row[3], cls=CJsonEncoder).replace("\"", "")
            userList.append(dict)
        return userList
    def getUserInfoById(self,id):
        db = DBUtil()
        data = self.db.execute_select("SELECT * FROM user_login WHERE ID=%S",id)
        return data
    def getUserInfoByName(self,username):
        db = DBUtil()
        data = db.execute_select("SELECT * FROM user_login WHERE USERNAME=%s",username)
        #得到元组，转成字典
        dict = {}
        if data:
            data = data[0]
            dict['userid'] = data[0]
            dict['username'] = data[1]
            dict['password'] = data[2]
            dict['CREATE_TIME'] = data[3]
        return dict
if __name__ == "__main__":
    db = UserInfoDao()
    db.addUserInfo('www','1111','2018-02-25 17:29:11')

