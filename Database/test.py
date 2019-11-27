import mysql.connector

db=mysql.connector.connect(
      host="localhost",
      user="root",
      password="root",
      database="cse"
)

cursor=db.cursor()

cursor.execute("delete from mytable where age=25")

db.commit()

