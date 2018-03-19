from myblog.mysql.DBUtil import DBUtil
from myblog.mysql.CJsonEncoder import CJsonEncoder
import json
class UserDailyCategoryDao:
    def __init__(self):
        self.db = DBUtil()
    def addUserDailyDetail(self,category_id,daily_id):
        db = DBUtil()
        sql = 'insert into `USER_DAILY_DETAILS` VALUE(id,%d,%d)'%(category_id,daily_id)
        db.execute_insert(sql)
    def getUserDailyDetailById(self,category_id,daily_id):
        db = DBUtil()
        sql = 'SELECT * FROM `USER_DAILY_DETAILS` WHERE USER_CATEGORY_ID=%d AND DAILY_ID=%d'%(category_id,daily_id)
        data = db.execute(sql)
        if data:
            # 存在数据
            return True
        else:
            # 不存在数据
            return False




