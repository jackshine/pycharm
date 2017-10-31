#encoding=utf8
import pymysql
db = pymysql.connect("localhost","root","","test")
cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print("database version:%s" %data)
db.close()