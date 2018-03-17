from myblog.mysql.DBUtil import DBUtil
from myblog.mysql.CJsonEncoder import CJsonEncoder
import json
class UserTag:
    def __init__(self):
        self.db = DBUtil()
    def addUserTag(self,userid,tag):
        #USERID INT PRIMARY KEY,USERNAME VARCHAR(20),PASSWORD VARCHAR(32),REGTIME DATETIME,DELFLAG INT
        db = DBUtil()
        db.execute_insert('insert into `USER_DAILY_TAGS` VALUE(id,%s,%s)',(userid,tag))
    def getAllUserInfo(self):
      pass

