import mysql.connector
db=mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      database="cseb"
)

cursor=db.cursor()
query="insert into trainees(name,age) values(%s,%s)"
values=("Raja",26)

cursor.execute(query,values)
db.commit()

#select * from bme