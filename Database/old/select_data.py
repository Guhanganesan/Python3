import mysql.connector

db=mysql.connector.connect(
      host="localhost",
      user="root",
      password="root",
      database="mydb"
)

cursor=db.cursor()

cursor.execute("select * from mytable")

result=cursor.fetchall()

for x in result:
    print(x)

