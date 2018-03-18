from myblog.mysql.DBUtil import DBUtil
from myblog.mysql.CJsonEncoder import CJsonEncoder
import json
class UserCategoryDao:
    def __init__(self):
        self.db = DBUtil()
    def addUserDailyDetail(category_id,daily_id):
        db = DBUtil()
        sql = 'insert into `USER_DAILY_DETAILS` VALUE(id,%d,%d)'%(category_id,daily_id)
        db.execute_insert(sql)



