import mysql.connector
db=mysql.connector.connect(
      host="localhost",
      user="root",
      password="root",
      database="cse"
)

cursor=db.cursor()
cursor.execute("select * from mytable where age=27")
result=cursor.fetchall()

for x in result:
    print(x)


