import mysql.connector
db=mysql.connector.connect(
      host="localhost",
      user="root",
      password="root",
      database="3edge"
)

cursor=db.cursor()
query="insert into trainees(name,age) values(%s,%s)"
values=("murugan",28)

cursor.execute(query,values)
db.commit()
