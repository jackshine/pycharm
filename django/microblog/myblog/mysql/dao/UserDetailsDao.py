from myblog.mysql.DBUtil import DBUtil
from myblog.mysql.CJsonEncoder import CJsonEncoder
import json


class UserDetailsDao:
    def __init__(self):
        self.db = DBUtil()

    def addUserDetail(self, user_login_id, gender, img_path, birthday, province, city, marriage):
        #
        db = DBUtil()
        db.execute_insert('insert into user_details VALUE(id,%s,%s,%s,%s,%s,%s,%s)',
                          (user_login_id, gender, img_path, birthday, province, city, marriage))

    def getUserDetail(self, user_login_id):
        db = DBUtil()
        data = db.execute_select('select * from user_details where user_login_id = %s', user_login_id)
        print('************')
        print(data)
        print('************')
        if data:
            row = data[0]
            user_details = {}
            user_details['id'] = row[0]
            user_details['user_login_id'] = row[1]
            user_details['gender'] = row[2]
            user_details['img_path'] = row[3]
            user_details['birthday'] = row[4]
            user_details['province'] = row[5]
            user_details['city'] = row[6]
            user_details['marriage'] = row[7]
            return row
        else:
            return False

    def updateUserDetail(self, user_login_id, gender, img_path, birthday, province, city, marriage):
        db = DBUtil()
        db.execute(
            "UPDATE `user_details` SET gender=%s,img_path='%s',birthday='%s',province=%s,city=%s,marriage=%s  WHERE user_login_id = %s"%(gender, img_path, birthday, province, city, marriage, user_login_id))
