import csv
import pandas as pd
import time

strt=time.time()

def fact(str):


   path ="C:\\Users\\datapro.csv"
   file=open(path,newline='')
   reader = csv.reader(file)
   #df = pd.read_csv("C:\\Users\\datapro.csv",engin="python")


   list1=[]
   dic1={}


   for i in reader:
       for j in reader:
          dic1[i[8]]=list(dict.fromkeys(list1.append(j[7])))

   print("District :")
   if str in dic1:
     print(dic1[str])






def fact1(str2):

   path ="C:\\Users\\datapro.csv"
   file=open(path,newline='')
   reader = csv.reader(file)
   Stack2 = []
   dic2={}
   for j in reader:
       for k in reader:
          dic2[j[7]]=Stack2.append(k[4])

   print("Pincode :")
   if str2 in dic2:
      print(dic2[str2])


str=input("enter state")
fact(str)
str2=input("enter District :")
fact1(str2)

last = time.time()


print("execution time",last-strt)














