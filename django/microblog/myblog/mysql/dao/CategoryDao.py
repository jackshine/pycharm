from myblog.mysql.DBUtil import DBUtil
class CategoryDao:
    def __init__(self):
        self.db = DBUtil()
    def addCategory(self,name):
        #USERID INT PRIMARY KEY,USERNAME VARCHAR(20),PASSWORD VARCHAR(32),REGTIME DATETIME,DELFLAG INT
        db = DBUtil()
        db.execute_insert('insert into Category VALUE(id,%s)',(name))
    def getAllCategory(self):
        pass
    def getCategoryById(self,id):
        pass
    def getCategoryByName(self,username):
        pass

