import mysql.connector
db=mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      database="cseb"
)

cursor=db.cursor()
cursor.execute("create table trainees(name varchar(30), age varchar(30))")

#use db;
#show tables;