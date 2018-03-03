from myblog.mysql.DBUtil import DBUtil
from myblog.mysql.CJsonEncoder import CJsonEncoder
import json
class DailyDao:
    def __init__(self):
        self.db = DBUtil()
    def addDaily(self,title,body,created_time,category,user_id):
        #USERID INT PRIMARY KEY,USERNAME VARCHAR(20),PASSWORD VARCHAR(32),REGTIME DATETIME,DELFLAG INT
        db = DBUtil()
        db.execute_insert('insert into daily VALUE(id,%s,%s,%s,%s)',(title,body,created_time,category,user_id))
    def getAllDaily(self):
        db = DBUtil()
        results = db.execute('SELECT d.`id`,d.`title`,d.`body`,d.`created_time`,d.`user_id`,u.`username` FROM `daily` d '
                         'INNER JOIN `userinfo` u ON  d.`user_id`=u.`id`')
        dataList = []
        for row in results:
            dict = {}
            dict['id'] = row[0]
            dict['title'] = row[1]
            dict['body'] = row[2]
            dict['created_time'] = row[3]
            dict['user_id'] = row[4]
            dict['user_name'] = row[5]
            dataList.append(dict)
        return dataList
    def getRecentDaily(self):
        db = DBUtil()
        results = db.execute('SELECT * FROM daily  ORDER BY created_time DESC  LIMIT 5')
        dataList = []
        for row in results:
            dict = {}
            dict['id'] = row[0]
            dict['title'] = row[1]
            dict['body'] = row[2]
            dict['created_time'] = row[3]
            dict['user_id'] = row[4]
            dict['user_name'] = row[5]
            dataList.append(dict)
        return dataList
    def getArchivesDaily(self):
        db = DBUtil()
        results = db.execute('SELECT COUNT(*) AS COUNT, DATE_FORMAT( created_time, \'%Y-%m\') AS created_time FROM daily GROUP BY DATE_FORMAT( created_time, \'%Y-%m\')  ORDER BY created_time DESC')
        dataList = []
        for row in results:
            dict = {}
            dict['count'] = row[0]
            dict['date'] = row[1]
            dict['year']  =row[1].split('-')[0]
            dict['month'] =row[1].split('-')[1]
            dataList.append(dict)
        print(dataList)
        return dataList

    def getCategoryDaily(self):
        #SELECT * FROM `category` c LEFT JOIN `daily` d ON c.`ID`=d.`category_id`
        db = DBUtil()
        results = db.execute(
            'SELECT * FROM `category`')
        dataList = []
        for row in results:
            dict = {}
            dict['id'] = row[0]
            dict['name'] = row[1]
            dataList.append(dict)
        print(dataList)
        return dataList
    def getDailyById(self,id):
        db = DBUtil()
        data = self.db.execute_select("SELECT * FROM USERINFO WHERE USERID=%S",id)
        return data
    def searchDailyByName(self,username):
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
    def search_daily(self,str):
        db = DBUtil()
        # str = like  '%str%'
        sql = "SELECT d.`id`,d.`title`,d.`body`,d.`created_time`,d.`user_id`,u.`username` FROM (SELECT * FROM daily WHERE title LIKE \'%"+str+"%\' or body LIKE \'%"+str+"%\' ) AS d INNER JOIN `userinfo` u ON  d.`user_id`=u.`id`"
        print(sql)
        results = db.execute(sql)
        dataList = []
        for row in results:
            dict = {}
            dict['id'] = row[0]
            dict['title'] = row[1]
            dict['body'] = row[2]
            print(json.dumps(row[3], cls=CJsonEncoder))
            dict['created_time'] =json.dumps(row[3], cls=CJsonEncoder).replace("\"","")
            dict['user_id'] = row[4]
            dict['user_name'] = row[5]
            dataList.append(dict)
        return dataList


