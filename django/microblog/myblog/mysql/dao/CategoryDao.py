from myblog.mysql.DBUtil import DBUtil


class CategoryDao:
    def __init__(self):
        self.db = DBUtil()

    def addCategory(self, name):
        # USERID INT PRIMARY KEY,USERNAME VARCHAR(20),PASSWORD VARCHAR(32),REGTIME DATETIME,DELFLAG INT
        db = DBUtil()
        db.execute_insert('insert into Category VALUE(id,%s)', (name))

    def getCategoryList(self):
        # SELECT * FROM `CATEGORY` c LEFT JOIN `daily` d ON c.`ID`=d.`category_id`
        db = DBUtil()
        results = db.execute('SELECT id,name FROM `CATEGORY`')
        dataList = []
        for row in results:
            dict = {}
            dict['id'] = row[0]
            dict['name'] = row[1]
            dataList.append(dict)
        return dataList

    def getCategoryById(self, id):
        pass

    def getCategoryByName(self, username):
        pass
