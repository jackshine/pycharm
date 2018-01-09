#encoding=utf8
import pymysql
db = pymysql.connect("localhost","root","","test")
cursor = db.cursor()
sql = "INSERT INTO STUDENT(NAME,AGE) VALUES(%s,%s)"%("'lin'","'123'")
print(sql)
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
db.close()


