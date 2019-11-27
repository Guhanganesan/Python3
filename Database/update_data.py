import mysql.connector

db=mysql.connector.connect(
      host="localhost",
      user="root",
      password="root",
      database="agni"
)

cursor=db.cursor()

cursor.execute("update bme set age=2  where name='Raja'")
db.commit()

#select * from bme;

