from myblog.mysql.DBUtil import DBUtil
class UserInfoDao:
    def __init__(self):
        self.db = DBUtil()
    def addUserInfo(self,username,password,regtime,delflag):
        #USERID INT PRIMARY KEY,USERNAME VARCHAR(20),PASSWORD VARCHAR(32),REGTIME DATETIME,DELFLAG INT
        self.db.execute_insert('insert into userinfo VALUE(userid,%s,%s,%s,%s)',(username,password,regtime,delflag))
    def getAllUserInfo(self):
        pass
    def getUserInfoById(self,id):
        data = self.db.execute_select("SELECT * FROM USERINFO WHERE USERID=%S",id)
        return data
    def getUserInfoByName(self,username):
        data = self.db.execute_select("SELECT * FROM USERINFO WHERE USERNAME=%s",username)
        #得到元组，转成字典
        dict = {}
        if data:
            data = data[0]
            dict['userid'] = data[0]
            dict['password'] = data[1]
            dict['regtime'] = data[2]
            dict['delflag'] = data[3]
        return dict

