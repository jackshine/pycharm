from myblog.mysql.DBUtil import DBUtil
from myblog.mysql.CJsonEncoder import CJsonEncoder
import json
class UserInfoDao:
    def __init__(self):
        self.db = DBUtil()
    def addUserInfo(self,username,password,create_time,role_id):
        #USERID INT PRIMARY KEY,USERNAME VARCHAR(20),PASSWORD VARCHAR(32),REGTIME DATETIME,DELFLAG INT
        db = DBUtil()
        sql = "INSERT INTO  `USER_LOGIN` VALUE(id,'%s','%s','%s',%d)"%(username,password,create_time,role_id)
        db.execute(sql)
    def getAllUserInfo(self):
      pass

    def searchUserInfo(self,str):
        db = DBUtil()
        sql = "SELECT * FROM `USER_LOGIN` WHERE USERNAME LIKE '%"+str+"%'"
        dataList = db.execute(sql)
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
        sql = "SELECT * FROM `USER_LOGIN` WHERE ID=%d"%id
        data = self.db.execute_select()
        return data
    def getUserInfoByName(self,username):
        db = DBUtil()
        data = db.execute_select("SELECT * FROM `USER_LOGIN` WHERE USERNAME=%s",username)
        #得到元组，转成字典
        dict = {}
        if data:
            data = data[0]
            dict['userid'] = data[0]
            dict['username'] = data[1]
            dict['password'] = data[2]
            dict['CREATE_TIME'] = data[3]
        return dict

