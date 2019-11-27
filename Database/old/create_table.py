import mysql.connector

db=mysql.connector.connect(
      host="localhost",
      user="root",
      password="root",
      database="mydb"
)

cursor=db.cursor()
cursor.execute("create table mytable(name varchar(30), age varchar(30))")

