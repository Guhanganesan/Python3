import mysql.connector

db=mysql.connector.connect(
      host="localhost",
      user="root",
      password="1234"
)
cursor=db.cursor()
cursor.execute("create database cseb")

#show databases;
#pip install mysql-connector-python

