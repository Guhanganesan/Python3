import mysql.connector

db=mysql.connector.connect(
      host="localhost",
      user="root",
      password="root",
      database="mydb"
)

cursor=db.cursor()

cursor.execute("show tables")

for x in cursor:
    print(x)



















