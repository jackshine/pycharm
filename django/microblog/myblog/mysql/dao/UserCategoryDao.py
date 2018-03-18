from myblog.mysql.DBUtil import DBUtil
from myblog.mysql.CJsonEncoder import CJsonEncoder
import json
class UserCategoryDao:
    def __init__(self):
        self.db = DBUtil()
    def addUserCategory(self,user_id,daily_id,category_name,isDelete):
        #USERID INT PRIMARY KEY,USERNAME VARCHAR(20),PASSWORD VARCHAR(32),REGTIME DATETIME,DELFLAG INT
        db = DBUtil()
        sql = 'insert into `USER_CATEGORY` VALUE(id,%d,"%s")'%(user_id,daily_id,category_name,isDelete)
        id = db.execute_insert(sql)
        return id

    def getUserCategory(self,user_id):
        db = DBUtil()
        sql = "SELECT ID,CATEGORY_NAME FROM `USER_CATEGORY` WHERE USER_LOGIN_ID =%s AND IS_DELETE=0"%user_id
        data = db.execute(sql)
        user_category_list = []
        if data:
            for row in data:
                dict = {}
                dict['id'] = row[0]
                dict['name'] = row[1]
                user_category_list.append(dict)
        print(user_category_list)
        return user_category_list
    def getUserCategoryByName(self,user_login_id,categoryName):
        db = DBUtil()
        sql = "SELECT ID,CATEGORY_NAME FROM  `USER_CATEGORY` WHERE USER_LOGIN_ID =%s and CATEGORY_NAME='%s' AND IS_DELETE=0" % (user_login_id,categoryName)
        data = db.execute(sql)
        if data:
            return True
        else:
            return False



