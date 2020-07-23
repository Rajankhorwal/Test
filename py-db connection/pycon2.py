import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",password="rajan@24")

print(mydb)
mycursor=mydb.cursor()


mycursor.execute("show databases")
for db in mycursor:
    print(db)