from myblog.mysql.DBUtil import DBUtil
from myblog.mysql.CJsonEncoder import CJsonEncoder
import json


class UserImgDao:
    def __init__(self):
        self.db = DBUtil()

    def addUserImg(self, user_login_id, img_path):
        db = DBUtil()
        db.execute_insert('insert into user_img VALUE(id,%s,%s)', (img_path, user_login_id))

    def updateUserImg(self, user_login_id, img_path):
        db = DBUtil()
        db.execute("update `user_img` set img_path='%s' where user_login_id=%s" % (img_path, user_login_id))

    def getUserImgById(self, user_login_id):
        db = DBUtil()
        data = db.execute("select * from `user_img` where user_login_id=%s"%(user_login_id))
        if data:
            return True
        else:
            return False

