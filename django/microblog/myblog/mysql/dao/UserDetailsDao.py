from myblog.mysql.DBUtil import DBUtil
from myblog.mysql.CJsonEncoder import CJsonEncoder
import json
class UserDetailsDao:
    def __init__(self):
        self.db = DBUtil()
    def addUserDetail(self,username,password,create_time):
        #USERID INT PRIMARY KEY,USERNAME VARCHAR(20),PASSWORD VARCHAR(32),REGTIME DATETIME,DELFLAG INT
        db = DBUtil()
        db.execute_insert('insert into userinfo VALUE(id,%s,%s,%s)',(username,password,create_time))
    def getAllUserInfo(self):
      pass



