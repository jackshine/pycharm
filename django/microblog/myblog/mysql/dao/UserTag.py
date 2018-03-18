from myblog.mysql.DBUtil import DBUtil
from myblog.mysql.CJsonEncoder import CJsonEncoder
import json
class UserTag:
    def __init__(self):
        self.db = DBUtil()
    def addUserTag(self,userid,daily_id,tag):
        #USERID INT PRIMARY KEY,USERNAME VARCHAR(20),PASSWORD VARCHAR(32),REGTIME DATETIME,DELFLAG INT
        db = DBUtil()
        sql = 'insert into `USER_DAILY_TAGS` VALUE(id,%d,%d,"%s")'%(userid,daily_id,tag)
        id = db.execute_insert(sql)
        return id
    def getAllUserInfo(self):
      pass

