from django.http import HttpResponse
from django.shortcuts import render

import pymysql


def index(request):
    return render(request,'webdata.html')


def func(request):
    result = request.GET['schem']

    mydb = pymysql.connect(host="localhost", user="root", password="rajan@24",database="student")
    mycursor = mydb.cursor()
    str="select * from {}".format(result)
    names=[]
    mycursor.execute(str)
    for row in mycursor.fetchall():
        names.append(row)

    mydb.close()

    return render(request,'webdata1.html',{'var':names})

def func1(request):
    res = request.GET['sch']

    mydb = pymysql.connect(host="localhost", user="root", password="rajan@24", database="student")
    mycursor = mydb.cursor()
    str = "select {} from student1".format(res)
    names1 = []
    mycursor.execute(str)
    for row in mycursor.fetchall():
        names1.append(row)

    return render(request, 'webdata1.html', {'var1': names1})

def func2(request):
    res = request.GET['sch1']

    mydb = pymysql.connect(host="localhost", user="root", password="rajan@24", database="student")
    mycursor = mydb.cursor()
    str = "select {} from employ".format(res)
    names2= []
    mycursor.execute(str)
    for row in mycursor.fetchall():
        names2.append(row)

    return render(request, 'webdata1.html', {'var2': names2})



