import mysql.connector

db=mysql.connector.connect(
      host="localhost",
      user="root",
      password=""
)
cursor=db.cursor()
cursor.execute("create database cseb")

#show databases;
#pip install mysql-connector-python

