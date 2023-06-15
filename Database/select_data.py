import mysql.connector
db=mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      database="cseb"
)
cursor=db.cursor()

cursor.execute("select * from trainees")

result=cursor.fetchall()

for x in result:
    print(x)


