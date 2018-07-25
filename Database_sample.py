import xlrd
import pymysql
import xlwt


conn = pymysql.connect(port=3306,host='localhost', user='root', passwd='admin123', db='pythondb')

cur = conn.cursor()

#cur.execute('create table empinfo (id INT AUTO_INCREMENT PRIMARY KEY,name varchar(20),dept varchar(10),salary int(10))')
#cur.execute('insert into empinfo values(1,\'Thomas1\',\'Sales\',5000)')
#cur.execute('insert into empinfo values(2,\'Thomas2\',\'Sales\',6000)')
#cur.execute('insert into empinfo values(3,\'Thomas3\',\'Sales\',7000)')
#cur.execute('insert into empinfo values(4,\'Thomas4\',\'Sales\',25000)')
cur.execute('select * from empinfo')
print(cur.fetchone())

conn.commit()