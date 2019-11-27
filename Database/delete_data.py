import mysql.connector

db=mysql.connector.connect(
      host="localhost",
      user="root",
      password="root",
      database="agni"
)

cursor=db.cursor()

cursor.execute("delete from bme where age=27")

db.commit()



# select * from bme;
