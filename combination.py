# from itertools import combinations
#
# dict1=[]
#
# set = {5,1,2}
# list1=list(set)
#
#
# for i in range(1,len(list1)+1):
#        dict1.append(list(combinations(list1, i)))
#
# print(dict1)
#
set1={3,2}
list1=list(set1)
t=set()


dict1=[]
dict2=[]

if len(list1)>3:
  for i in range(0,len(list1)):
     dict1.append({list1[i]})
     for j in range(i+1,len(list1)):

          dict1.append({list1[i],list1[j]})

  for i in range(0, len(list1) + 1):
     if i > 3:
         for i in range(0, len(dict1)):
             dict1.append(dict1[i].union(dict1[i + 1]))
  dict1.append(tuple(list1))
  dict1.append(())
  print(list(set([tuple(set(i)) for i in dict1])))

if len(list1)<=3:
   for i in range(0,len(list1)):
      dict1.append({list1[i]})
      for j in range(i+1,len(list1)):

         dict1.append({list1[i],list1[j]})


   t.update(list1)
   if len(list1)>2:
      dict1.append(t)

   dict1.append({})
   for i in dict1:
      dict2.append(tuple(i))
   print(dict2)

