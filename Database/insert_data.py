import mysql.connector
db=mysql.connector.connect(
      host="localhost",
      user="root",
      password="root",
      database="agni"
)

cursor=db.cursor()
query="insert into bme(name,age) values(%s,%s)"
values=("Raja",26)

cursor.execute(query,values)
db.commit()

#select * from bme