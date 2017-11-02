#encoding=utf8
import pymysql
db = pymysql.connect("localhost","root","","test")
cursor = db.cursor()
for i in  range(10):
    sql = "INSERT INTO STUDENT(NAME,AGE) VALUES(%s,%s)"%(i,i)
    print(sql)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
db.close()


