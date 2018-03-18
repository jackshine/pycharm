from myblog.mysql.DBUtil import DBUtil
from myblog.mysql.CJsonEncoder import CJsonEncoder
import json


class UserDetailsDao:
    def __init__(self):
        self.db = DBUtil()

    def addUserDetail(self, user_login_id, gender, img_path, birthday, province, city, marriage):
        #
        db = DBUtil()
        db.execute_insert('insert into `USER_DETAILS` VALUE(id,%s,%s,%s,%s,%s,%s,%s)',
                          (user_login_id, gender, img_path, birthday, province, city, marriage))

    def getUserDetail(self, user_login_id):
        print(user_login_id)
        db = DBUtil()
        data = db.execute_select('SELECT USER_LOGIN_ID,gender,IMG_PATH,BIRTHDAY,PROVINCE,CITY,MARRIAGE,l.`USERNAME` FROM `USER_DETAILS` d LEFT JOIN `USER_LOGIN` l ON  d.`USER_LOGIN_ID`=l.`ID` WHERE d.`USER_LOGIN_ID`=%s', user_login_id)
        if data:
            row = data[0]
            user_details = {}
            user_details['user_login_id'] = row[0]
            user_details['gender'] = row[1]
            user_details['img_path'] = row[2]
            user_details['birthday'] = row[3]
            user_details['province'] = row[4]
            user_details['city'] = row[5]
            user_details['marriage'] = row[6]
            user_details['username'] = row[7]
            db2 = DBUtil()
            region=  db2.execute_select("SELECT p.`code` p_code,c.`code` c_code,p.`name` p_name,c.`name` c_name FROM `province` p INNER JOIN `city` c ON c.`province_code` = p.`code` WHERE c.`code` = %s",user_details['city'])
            distict = {}
            if region:
                 temp = region[0]
                 distict['p_code']= temp[0]
                 distict['c_code']= temp[1]
                 distict['p_name']= temp[2]
                 distict['c_name']= temp[3]

            print('************')
            print(user_details)
            print('************')
            return (user_details,distict)
        else:
            return False

    def updateUserDetail(self, user_login_id, gender, img_path, birthday, province, city, marriage,name):
        db = DBUtil()
        db.execute(
            "UPDATE `user_details` SET gender=%s,img_path='%s',birthday='%s',province=%s,city=%s,marriage=%s  WHERE user_login_id = %s"%(gender, img_path, birthday, province, city, marriage, user_login_id))
        db = DBUtil()
        db.execute("UPDATE `user_login` SET USERNAME ='%s' WHERE id=%s"%(name,user_login_id))