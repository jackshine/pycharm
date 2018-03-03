from myblog.mysql.DBUtil import DBUtil
from myblog.mysql.CJsonEncoder import CJsonEncoder
import json
class UserInfoDao:
    def __init__(self):
        self.db = DBUtil()
    def addUserInfo(self,username,password,created_time):
        #USERID INT PRIMARY KEY,USERNAME VARCHAR(20),PASSWORD VARCHAR(32),REGTIME DATETIME,DELFLAG INT
        db = DBUtil()
        db.execute_insert('insert into userinfo VALUE(id,%s,%s,%s)',(username,password,created_time))
    def getAllUserInfo(self):
      pass

    def searchUserInfo(self,str):
        db = DBUtil()
        dataList = db.execute("select * from userinfo where username like '%"+str+"%'")
        dict = {}
        userList = []
        for row in dataList:
            dict['id'] = row[0]
            dict['username'] = row[1]
            dict['password'] = row[2]
            dict['created_time'] = json.dumps(row[3], cls=CJsonEncoder).replace("\"", "")
            userList.append(dict)
        return userList
    def getUserInfoById(self,id):
        db = DBUtil()
        data = self.db.execute_select("SELECT * FROM USERINFO WHERE ID=%S",id)
        return data
    def getUserInfoByName(self,username):
        db = DBUtil()
        data = db.execute_select("SELECT * FROM USERINFO WHERE USERNAME=%s",username)
        #得到元组，转成字典
        dict = {}
        if data:
            data = data[0]
            dict['userid'] = data[0]
            dict['username'] = data[1]
            dict['password'] = data[2]
            dict['CREATED_TIME'] = data[3]
        return dict

