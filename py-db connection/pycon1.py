import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",password="rajan@24",database="student")

print(mydb)

mycursor=mydb.cursor()


mycursor.execute("show tables")
for tb in mycursor:
    print(tb)