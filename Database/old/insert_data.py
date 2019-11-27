import mysql.connector

db=mysql.connector.connect(
      host="localhost",
      user="root",
      password="root",
      database="mydb"
)

cursor=db.cursor()
query="insert into mytable(name,age) values(%s,%s)"
values=("anbu",27)

cursor.execute(query,values)

db.commit()
