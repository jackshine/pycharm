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
    def getUserImg(self, user_login_id):
        db = DBUtil()
        data = db.execute("select img_path,user_login_id from `user_img` where user_login_id=%s"%(user_login_id))
        img_data = {}
        if data:
            row = data[0]
            img_data['img_path'] = '/'+row[0]
            img_data['user_login_id'] = row[1]
        else:
            return False
        return img_data
