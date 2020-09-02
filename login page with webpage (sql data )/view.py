from django.http import HttpResponse
from django.shortcuts import render, redirect
import csv
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


from django.contrib.auth.models import User


from itertools import groupby
from operator import itemgetter
import webbrowser

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

from .models import *
from .form1 import CreateUserForm
# from .filters import OrderFilter

import smtplib
import pymysql


def index(request):
    context = {}
    return render(request, 'webdata.html',context)


def func3(request):
    result = request.GET['schem']


    mydb = pymysql.connect(host="localhost", user="root", password="rajan@24", database="student")
    mycursor = mydb.cursor()
    list = []
    str = "select * from {}".format(result)
    mycursor.execute(str)

    name = mycursor.fetchall()

    for i in name:
        list.append(i)
    if result=='student1':

       fields = ['student_id', 'name', 'rollno', 'DOB']


       rows = list

       filename = "sqltable_record of {}.csv".format(result)

       with open(filename, 'w') as csvfile:

            csvwriter = csv.writer(csvfile)

            csvwriter.writerow(fields)

            csvwriter.writerows(rows)
       msg = MIMEMultipart()

       attachment = open(filename, 'rb')

       part = MIMEBase('application', 'octet-stream')
       part.set_payload((attachment).read())
       encoders.encode_base64(part)
       part.add_header('Content-Disposition', "attachment; filename= " + filename)

       msg.attach(part)
       text = msg.as_string()
       server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
       server.login("rajankhorwal75@gmail.com", "rajanjustinkidraul")
       subject = 'acknowledge as csv file'
       # body ='how about dinner at 6pm this saturday?'
       # msg=f'subject:{subject}\n\n{body}'
       server.sendmail("rajankhorwal75@gmail.com",request.user.email, text)
       server.quit()
    if result == 'employ':
        fields = ['id', 'emp_name', 'salary']

        rows = list

        filename = "sqltable_record of {}.csv".format(result)

        with open(filename, 'w') as csvfile:
            csvwriter = csv.writer(csvfile)

            csvwriter.writerow(fields)

            csvwriter.writerows(rows)
        msg = MIMEMultipart()

        attachment = open(filename, 'rb')

        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= " + filename)

        msg.attach(part)
        text = msg.as_string()
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login("rajankhorwal75@gmail.com", "rajanjustinkidraul")
        subject = 'acknowledge as csv file'
        # body ='how about dinner at 6pm this saturday?'
        # msg=f'subject:{subject}\n\n{body}'
        server.sendmail("rajankhorwal75@gmail.com",request.user.email, text)
        server.quit()

    # emails = User.objects.filter(is_active=False).values_list('email', flat=True)


    # server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    # server.login("rajankhorwal75@gmail.com", "rajanjustinkidraul")
    # subject = 'acknowledgement'
    # body = '{} table selected by {}'.format(result,request.user )
    # msg = f'subject:{subject}\n\n{body}'
    # server.sendmail("rajankhorwal75@gmail.com",request.user.email, msg)
    # server.quit()

    if result == 'student1':
        return render(request, 'webdata.html', {'call': 'continue'})
    if result == 'employ':
        return render(request, 'webdata.html', {'call1': 'continue1'})
    if result == 'student1':
        return redirect('func1')
    if result == 'employ':
        return redirect('func2')


# def func(request):
#     result = request.GET['schem']
#
#
#     mydb = pymysql.connect(host="localhost", user="root", password="rajan@24",database="student")
#     mycursor = mydb.cursor()
#     str="select * from {}".format(result)
#     names2=[]
#     names1=[]
#     names=[]
#     mycursor.execute(str)
#     name=mycursor.fetchall()
#     for i in name:
#         names.append(i)
#
#     val=names[0]
#
#     for i in val:
#         names1.append(i)
#     val1 = names[1]
#
#     for i in val1:
#         names2.append(i)
#     names3=[]
#     val2 = names[2]
#
#     for i in val2:
#         names3.append(i)
#
#     names4 = []
#     val3 = names[3]
#
#     for i in val3:
#         names4.append(i)
#
#     names5 = []
#     val4 = names[4]
#
#     for i in val4:
#         names5.append(i)
#     # for i in names:
#     #     names1.append(i)
#     mydb.close()
#     if result=="student1":
#           n="studend_id"
#           a="name"
#           m="rollno"
#           e="DOB"
#
#
#
#           return render(request,'webdata.html',{'value':result,'var':names1,'var1':names2,'var2':names3,'var3':names4,'var4':names5,'col':n,'col1':a,'col2':m,'col3':e,'value2':'start'})
#     if result=="employ":
#           n="id"
#           a="emp_name"
#           m="salary"
#
#           return render(request, 'webdata.html',{'var': names1, 'var1': names2, 'var2': names3, 'var3': names4, 'var4': names5, 'col': n,'col1': a, 'col2': m})
#


def func1(request):
    removepunc = request.GET.get('removepunc', 'off')
    removepunc1 = request.GET.get('removepunc1', 'off')

    removepunc2 = request.GET.get('removepunc2', 'off')
    removepunc3 = request.GET.get('removepunc3', 'off')

    mydb = pymysql.connect(host="localhost", user="root", password="rajan@24", database="student")
    mycursor = mydb.cursor()
    if (removepunc == "on" and removepunc1 == "on" and removepunc2 == "on" and removepunc3 == "on"):

        str = "select * from student1"
        names1 = []
        list = []
        list1 = []
        list2 = []
        list3 = []
        mycursor.execute(str)
        # for row in mycursor.fetchall():
        #     names1.append(row)
        name = mycursor.fetchall()
        for i in name:
            names1.append(i)
        for i in names1:
            list2.append(i[0])
        for i in names1:
            list.append(i[1])
        for i in names1:
            list1.append(i[2])
        for i in names1:
            list3.append(i[3])

        colname = "name"
        colname1 = "rollno"
        colname2 = "student_id"
        colname3 = 'DOB'

        return render(request, 'webdata.html',
                      {'value6': 'start5', 'value5': 'start4', 'value4': 'start3', 'value2': 'start', 'var10': list,
                       'var11': list1,
                       'column': colname, 'colname2': colname2, 'var12': list2, 'var13': list3, 'colname3': colname3,
                       'colname1': colname1, 'call': 'continue'})

    if (removepunc == "on" and removepunc1 == "on" and removepunc2 == "on"):

        str = "select * from student1"
        names1 = []
        list = []
        list1 = []
        list2 = []
        mycursor.execute(str)
        # for row in mycursor.fetchall():
        #     names1.append(row)
        name = mycursor.fetchall()
        for i in name:
            names1.append(i)
        for i in names1:
            list2.append(i[0])
        for i in names1:
            list.append(i[1])
        for i in names1:
            list1.append(i[2])

        colname = "name"
        colname1 = "rollno"
        colname2 = "student_id"

        return render(request, 'webdata.html',
                      {'value5': 'start4', 'value4': 'start3', 'value2': 'start', 'var10': list, 'var11': list1,
                       'column': colname, 'colname2': colname2, 'var12': list2,
                       'colname1': colname1, 'call': 'continue'})
    if (removepunc == "on" and removepunc1 == "on" and removepunc3 == "on"):

        str = "select * from student1"
        names1 = []
        list = []
        list1 = []
        list2 = []
        mycursor.execute(str)
        # for row in mycursor.fetchall():
        #     names1.append(row)
        name = mycursor.fetchall()
        for i in name:
            names1.append(i)
        for i in names1:
            list2.append(i[0])
        for i in names1:
            list.append(i[1])
        for i in names1:
            list1.append(i[3])

        colname = "name"
        colname1 = "DOB"
        colname2 = "student_id"

        return render(request, 'webdata.html',
                      {'value5': 'start4', 'value4': 'start3', 'value2': 'start', 'var10': list, 'var11': list1,
                       'column': colname, 'colname2': colname2, 'var12': list2,
                       'colname1': colname1, 'call': 'continue'})
    if (removepunc1 == "on" and removepunc2 == "on" and removepunc3 == "on"):

        str = "select * from student1"
        names1 = []
        list = []
        list1 = []
        list2 = []
        mycursor.execute(str)
        # for row in mycursor.fetchall():
        #     names1.append(row)
        name = mycursor.fetchall()
        for i in name:
            names1.append(i)
        for i in names1:
            list2.append(i[1])
        for i in names1:
            list.append(i[2])
        for i in names1:
            list1.append(i[3])

        colname = "rollno"
        colname1 = "DOB"
        colname2 = "name"

        return render(request, 'webdata.html',
                      {'value5': 'start4', 'value4': 'start3', 'value2': 'start', 'var10': list, 'var11': list1,
                       'column': colname, 'colname2': colname2, 'var12': list2,
                       'colname1': colname1, 'call': 'continue'})
    if (removepunc == "on" and removepunc1 == "on"):

        str = "select * from student1"
        names1 = []
        list = []
        list1 = []
        mycursor.execute(str)
        # for row in mycursor.fetchall():
        #     names1.append(row)
        name = mycursor.fetchall()
        for i in name:
            names1.append(i)
        for i in names1:
            list.append(i[0])
        for i in names1:
            list1.append(i[1])

        colname = "student_id"
        colname1 = "name"
        return render(request, 'webdata.html',
                      {'value4': 'start3', 'value2': 'start', 'var10': list, 'var11': list1, 'column': colname,
                       'colname1': colname1, 'call': 'continue'})

    if (removepunc == "on" and removepunc2 == "on"):

        str = "select * from student1"
        names1 = []
        list = []
        list1 = []
        mycursor.execute(str)
        # for row in mycursor.fetchall():
        #     names1.append(row)
        name = mycursor.fetchall()
        for i in name:
            names1.append(i)
        for i in names1:
            list.append(i[0])
        for i in names1:
            list1.append(i[2])

        colname = "student_id"
        colname1 = "rollno"

        return render(request, 'webdata.html',
                      {'value4': 'start3', 'value2': 'start', 'var10': list, 'var11': list1, 'column': colname,
                       'colname1': colname1, 'call': 'continue'})

    if (removepunc == "on" and removepunc3 == "on"):

        str = "select * from student1"
        names1 = []
        list = []
        list1 = []
        mycursor.execute(str)
        # for row in mycursor.fetchall():
        #     names1.append(row)
        name = mycursor.fetchall()
        for i in name:
            names1.append(i)
        for i in names1:
            list.append(i[0])
        for i in names1:
            list1.append(i[3])

        colname = "Student_id"
        colname1 = "DOB"

        return render(request, 'webdata.html',
                      {'value4': 'start3', 'value2': 'start', 'var10': list, 'var11': list1, 'column': colname,
                       'colname1': colname1, 'call': 'continue'})
    if (removepunc1 == "on" and removepunc2 == "on"):

        str = "select * from student1"
        names1 = []
        list = []
        list1 = []
        mycursor.execute(str)
        # for row in mycursor.fetchall():
        #     names1.append(row)
        name = mycursor.fetchall()
        for i in name:
            names1.append(i)
        for i in names1:
            list.append(i[1])
        for i in names1:
            list1.append(i[2])

        colname = "name"
        colname1 = "rollno"
        return render(request, 'webdata.html',
                      {'value4': 'start3', 'value2': 'start', 'var10': list, 'var11': list1, 'column': colname,
                       'colname1': colname1, 'call': 'continue'})

    if (removepunc1 == "on" and removepunc3 == "on"):

        str = "select * from student1"
        names1 = []
        list = []
        list1 = []
        mycursor.execute(str)
        # for row in mycursor.fetchall():
        #     names1.append(row)
        name = mycursor.fetchall()
        for i in name:
            names1.append(i)
        for i in names1:
            list.append(i[1])
        for i in names1:
            list1.append(i[3])

        colname = "name"
        colname1 = "DOB"

        return render(request, 'webdata.html',
                      {'value4': 'start3', 'value2': 'start', 'var10': list, 'var11': list1, 'column': colname,
                       'colname1': colname1, 'call': 'continue'})
    if (removepunc2 == "on" and removepunc3 == "on"):

        str = "select * from student1"
        names1 = []
        list = []
        list1 = []
        mycursor.execute(str)
        # for row in mycursor.fetchall():
        #     names1.append(row)
        name = mycursor.fetchall()
        for i in name:
            names1.append(i)
        for i in names1:
            list.append(i[2])
        for i in names1:
            list1.append(i[3])

        colname = "rollno"
        colname1 = "DOB"

        return render(request, 'webdata.html',
                      {'value4': 'start3', 'value2': 'start', 'var10': list, 'var11': list1, 'column': colname,
                       'colname1': colname1, 'call': 'continue'})
    if removepunc == "on":
        str = "select * from student1"
        names1 = []
        list = []
        mycursor.execute(str)
        # for row in mycursor.fetchall():
        #     names1.append(row)
        name = mycursor.fetchall()
        for i in name:
            names1.append(i)
        for i in names1:
            list.append(i[0])

        colname = "student_id"

        return render(request, 'webdata.html',
                      {'value2': 'start', 'var10': list, 'column': colname, 'call': 'continue'})
    if removepunc1 == "on":
        str = "select * from student1"
        names1 = []
        list = []
        mycursor.execute(str)
        # for row in mycursor.fetchall():
        #     names1.append(row)
        name = mycursor.fetchall()
        for i in name:
            names1.append(i)
        for i in names1:
            list.append(i[1])
        colname = "name"

        return render(request, 'webdata.html',
                      {'value2': 'start', 'var10': list, 'column': colname, 'call': 'continue'})

    if removepunc2 == "on":
        str = "select * from student1"
        names1 = []
        list = []
        mycursor.execute(str)
        # for row in mycursor.fetchall():
        #     names1.append(row)
        name = mycursor.fetchall()
        for i in name:
            names1.append(i)
        for i in names1:
            list.append(i[2])
        colname = "rollno"

        return render(request, 'webdata.html',
                      {'value2': 'start', 'var10': list, 'column': colname, 'call': 'continue'})
    if removepunc3 == "on":
        str = "select * from student1"
        names1 = []
        list = []
        mycursor.execute(str)
        # for row in mycursor.fetchall():
        #     names1.append(row)
        name = mycursor.fetchall()
        for i in name:
            names1.append(i)
        for i in names1:
            list.append(i[3])
        colname = "DOB"

        return render(request, 'webdata.html',
                      {'value2': 'start', 'var10': list, 'column': colname, 'call': 'continue'})
    else:
        return render(request, 'webdata.html', {'call': 'continue'})


def func2(request):
    removepunc6 = request.GET.get('removepunc6', 'off')
    removepunc7 = request.GET.get('removepunc7', 'off')
    removepunc8 = request.GET.get('removepunc8', 'off')

    mydb = pymysql.connect(host="localhost", user="root", password="rajan@24", database="student")
    mycursor = mydb.cursor()
    if (removepunc6 == "yes" and removepunc7 == "yes" and removepunc8 == "yes"):

        str = "select * from employ"
        names1 = []
        list = []
        list1 = []
        list2 = []
        mycursor.execute(str)
        # for row in mycursor.fetchall():
        #     names1.append(row)
        name = mycursor.fetchall()
        for i in name:
            names1.append(i)
        for i in names1:
            list2.append(i[0])
        for i in names1:
            list.append(i[1])
        for i in names1:
            list1.append(i[2])

        colname = "emp_name"
        colname1 = "salary"
        colname2 = "id"

        return render(request, 'webdata.html',
                      {'value5': 'start4', 'value4': 'start3', 'value2': 'start', 'var10': list, 'var11': list1,
                       'column': colname, 'colname2': colname2, 'var12': list2,
                       'colname1': colname1, 'call1': 'continue1'})

    if (removepunc6 == "yes" and removepunc7 == "yes"):

        str = "select * from employ"
        names1 = []
        list = []
        list1 = []
        mycursor.execute(str)
        # for row in mycursor.fetchall():
        #     names1.append(row)
        name = mycursor.fetchall()
        for i in name:
            names1.append(i)
        for i in names1:
            list.append(i[0])
        for i in names1:
            list1.append(i[1])

        colname = "id"
        colname1 = "emp_name"
        return render(request, 'webdata.html',
                      {'value4': 'start3', 'value2': 'start', 'var10': list, 'var11': list1, 'column': colname,
                       'colname1': colname1, 'call1': 'continue1'})

    if (removepunc6 == "yes" and removepunc8 == "yes"):

        str = "select * from employ"
        names1 = []
        list = []
        list1 = []
        mycursor.execute(str)
        # for row in mycursor.fetchall():
        #     names1.append(row)
        name = mycursor.fetchall()
        for i in name:
            names1.append(i)
        for i in names1:
            list.append(i[0])
        for i in names1:
            list1.append(i[2])

        colname = "id"
        colname1 = "salary"

        return render(request, 'webdata.html',
                      {'call1': 'continue1', 'value4': 'start3', 'value2': 'start', 'var10': list, 'var11': list1,
                       'column': colname, 'colname1': colname1})

    if (removepunc7 == "yes" and removepunc8 == "yes"):

        str = "select * from employ"
        names1 = []
        list = []
        list1 = []
        mycursor.execute(str)
        # for row in mycursor.fetchall():
        #     names1.append(row)
        name = mycursor.fetchall()
        for i in name:
            names1.append(i)
        for i in names1:
            list.append(i[1])
        for i in names1:
            list1.append(i[2])

        colname = "emp_name"
        colname1 = "salary"

        return render(request, 'webdata.html',
                      {'call1': 'continue1', 'value4': 'start3', 'value2': 'start', 'var10': list, 'var11': list1,
                       'column': colname, 'colname1': colname1})

    if removepunc6 == "yes":
        str = "select * from employ"
        names1 = []
        list = []
        mycursor.execute(str)
        # for row in mycursor.fetchall():
        #     names1.append(row)
        name = mycursor.fetchall()
        for i in name:
            names1.append(i)
        for i in names1:
            list.append(i[0])

        colname = "id"

        return render(request, 'webdata.html',
                      {'call1': 'continue1', 'value3': 'start1', 'var10': list, 'column': colname})
    if removepunc7 == "yes":
        str = "select * from employ"
        names1 = []
        list = []
        mycursor.execute(str)
        # for row in mycursor.fetchall():
        #     names1.append(row)
        name = mycursor.fetchall()
        for i in name:
            names1.append(i)
        for i in names1:
            list.append(i[1])
        colname = "emp_name"

        return render(request, 'webdata.html',
                      {'call1': 'continue1', 'value3': 'start1', 'var10': list, 'column': colname})
    if removepunc8 == "yes":
        str = "select * from employ"
        names1 = []
        list = []
        mycursor.execute(str)
        # for row in mycursor.fetchall():
        #     names1.append(row)
        name = mycursor.fetchall()
        for i in name:
            names1.append(i)
        for i in names1:
            list.append(i[2])
        colname = "salary"

        return render(request, 'webdata.html',
                      {'call1': 'continue1', 'value3': 'start1', 'var10': list, 'column': colname})

    else:
        return render(request, 'webdata.html', {'call1': 'continue1'})

# def func2(request):
#     res = request.GET['sch1']
#
#     mydb = pymysql.connect(host="localhost", user="root", password="rajan@24", database="student")
#     mycursor = mydb.cursor()
#     str = "select {} from employ".format(res)
#     names2= []
#     mycursor.execute(str)
#     for row in mycursor.fetchall():
#         names2.append(row)
#
#     return render(request, 'webdata.html', {'var2': names2})


# def demo(request):
#
#
#     mydb = pymysql.connect(host="localhost", user="root", password="rajan@24",database="student")
#     mycursor = mydb.cursor()
#     str="select * from student1"
#     mycursor.execute(str)
#     result=mycursor.fetchall()
#     mydb.close()
#
#
#     return render(request,'webdata1.html',{'var':result})
# def fact(request):
#     value = request.GET['number']
#
#
#
#     mydb = pymysql.connect(host="localhost", user="root", password="rajan@24",database="student")
#     mycursor = mydb.cursor()
#     str="select * from student1"
#     names2=[]
#     names1=[]
#     names=[]
#     mycursor.execute(str)
#     name=mycursor.fetchall()
#     for i in name:
#         names.append(i)
#     if value=="1":
#          val=names[0]
#
#          for i in val:
#              names1.append(i)
#
#          n = "studend_id"
#          a = "name"
#          m = "rollno"
#          e = "DOB"
#
#          return render(request, 'webdata.html', {'value':'student1','var': names1,'col':n,'col1':a,'col2':m,'col3':e})
#     elif value=="2":
#         val = names[0]
#
#         for i in val:
#             names1.append(i)
#         val1 = names[1]
#
#         for i in val1:
#             names2.append(i)
#         n = "studend_id"
#         a = "name"
#         m = "rollno"
#         e = "DOB"
#
#         return render(request, 'webdata.html',{'value':'student1','var':names1,'var1':names2,'col':n,'col1':a,'col2':m,'col3':e})
#     elif value=="3":
#         val = names[0]
#
#         for i in val:
#             names1.append(i)
#         val1 = names[1]
#
#         for i in val1:
#             names2.append(i)
#
#         names3=[]
#         val2 = names[2]
#
#         for i in val2:
#             names3.append(i)
#         n = "studend_id"
#         a = "name"
#         m = "rollno"
#         e = "DOB"
#
#         return render(request, 'webdata.html', {'value':'student1','var': names1, 'var1': names2,'var2':names3,'col':n,'col1':a,'col2':m,'col3':e})
#     elif value=="4":
#         val = names[0]
#
#         for i in val:
#             names1.append(i)
#         val1 = names[1]
#
#         for i in val1:
#             names2.append(i)
#
#         names3 = []
#         val2 = names[2]
#
#         for i in val2:
#             names3.append(i)
#         names4 = []
#         val3 = names[3]
#
#         for i in val3:
#             names4.append(i)
#         n = "studend_id"
#         a = "name"
#         m = "rollno"
#         e = "DOB"
#
#         return render(request, 'webdata.html', {'value':'student1','var': names1, 'var1': names2, 'var2': names3,'var3':names4,'col':n,'col1':a,'col2':m,'col3':e})
#
#     elif value=="5":
#         val = names[0]
#
#         for i in val:
#             names1.append(i)
#         val1 = names[1]
#
#         for i in val1:
#             names2.append(i)
#
#         names3 = []
#         val2 = names[2]
#
#         for i in val2:
#             names3.append(i)
#         names4 = []
#         val3 = names[3]
#
#         for i in val3:
#             names4.append(i)
#
#         names5 = []
#         val4 = names[4]
#
#         for i in val4:
#             names5.append(i)
#         n = "studend_id"
#         a = "name"
#         m = "rollno"
#         e = "DOB"
#
#         return render(request, 'webdata.html',{'value':'student1','var': names1, 'var1': names2, 'var2': names3, 'var3': names4, 'var4': names5,'col':n,'col1':a,'col2':m,'col3':e})
#     # for i in names:
#     #     names1.append(i)
#     mydb.close()


# mytuple = sorted(names)
# FULL_HTML = []
#
# for name, rows in groupby(mytuple, itemgetter(0)):
#   table = []
#   for name, value1, value2 in rows:
#     table.append(
#         "<tr><td>{}</td><td>{}</td><td>{}</td><td></tr>".format(
#             name, value1, value2))
#
#   table = "<table>\n{}\n</table>".format('\n'.join(table))
#   FULL_HTML.append(table)
#
# FULL_HTML = "{}".format('\n'.join(FULL_HTML))
#





