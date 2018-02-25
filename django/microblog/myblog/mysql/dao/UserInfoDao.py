from myblog.mysql.DBUtil import DBUtil
class UserInfoDao:
    def __init__(self):
        self.db = DBUtil()
    def addUserInfo(self,username,password,regtime,**kwargs):
        #USERID INT PRIMARY KEY,USERNAME VARCHAR(20),PASSWORD VARCHAR(32),REGTIME DATETIME,DELFLAG INT
        db = DBUtil()
        db.execute_insert('insert into userinfo VALUE(userid,%s,%s,%s,%s)',(username,password,regtime,kwargs['delflag']))
    def getAllUserInfo(self):
        pass
    def getUserInfoById(self,id):
        db = DBUtil()
        data = self.db.execute_select("SELECT * FROM USERINFO WHERE USERID=%S",id)
        return data
    def getUserInfoByName(self,username):
        db = DBUtil()
        data = db.execute_select("SELECT * FROM USERINFO WHERE USERNAME=%s",username)
        #得到元组，转成字典
        dict = {}
        if data:
            data = data[0]
            dict['userid'] = data[0]
            dict['username'] = data[1]
            dict['password'] = data[2]
            dict['regtime'] = data[3]
            dict['delflag'] = data[4]
        return dict

