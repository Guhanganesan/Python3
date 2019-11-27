import mysql.connector

db=mysql.connector.connect(
      host="localhost",
      user="root",
      password="root",
      database="mydb"
)

cursor=db.cursor()

cursor.execute("update mytable set age=25 where name='anbu'")

db.commit()

