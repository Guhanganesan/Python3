import mysql.connector

db=mysql.connector.connect(
      host="localhost",
      user="root",
      password="root",
      database="mydb"
)

cursor=db.cursor()

cursor.execute("delete from mytable where age='28'")

db.commit()