import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",password="rajan@24",database="student")

print(mydb)

mycursor=mydb.cursor()


mycursor.execute("Create table student1(stud_id int(2),name varchar(10),rollno int(10))")