import mysql.connector as mysql

mydb = mysql.connect(
    host='localhost',
    user='root',
    password='',
    database='pythondemo'
)
# print(mydb)

# create db
mycursor = mydb.cursor()
mycursor.execute('CREATE DATABASE IF NOT EXISTS pythondemo')
mycursor.execute('CREATE TABLE IF NOT EXISTS user(id int(10) NOT NULL AUTO_INCREMENT PRIMARY KEY, name varchar(100))')
# mycursor.execute('SHOW DATABASES')

# for x in mycursor:
#     print(x)