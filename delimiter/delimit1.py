import mysql.connector
from new import fact

mydb = mysql.connector.connect(host="localhost", user="root", password="rajan@24", database="student")

print(mydb)

mycursor=mydb.cursor()

SQL= """USE student; 
        DELIMITER $$ 
        CREATE PROCEDURE delimit5() 
        BEGIN 
       Create table student8(stud_id int(2),name varchar(10),rollno int(10));
        END$$ 
        DELIMITER;"""
for i in mycursor.execute(fact(SQL), multi=True):
    pass

mycursor.callproc('delimit5')
for result in mycursor.stored_results():
    print(result.fetchall())



mydb.commit()

mycursor.close()
mydb.close()
mydb.disconnect()

