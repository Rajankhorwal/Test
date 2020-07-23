import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",password="rajan@24",database="student")

print(mydb)

mycursor=mydb.cursor()

sqlform="Insert into student1(stud_id,name,rollno) values(%s,%s,%s)"

stud=[(1,"rajan","015"),(2,"rajeev","026")]

mycursor.executemany(sqlform,stud)

mydb.commit()


