#by importing concuurent.futures

import time
import concurrent.futures
start=time.perf_counter()



def name(sec):
    print("hello",{sec})
    time.sleep(sec)
    return 'bye',{sec}



with concurrent.futures.ThreadPoolExecutor() as executor:
     seq=[6,4,7,2]
     result=[executor.submit(name,i)for i in seq]
     for i in concurrent.futures.as_completed(result):
         print(i.result())
#      result=executor.map(name,seq)
#      for result1 in result:
#          print(result1)

finish=time.perf_counter()
print("finished in",round(finish-start,2),"sec")

#by import threading

import threading
import time
import concurrent.futures
start=time.perf_counter()

def name(sec):
    print("hello",{sec})
    time.sleep(sec)
    print('bye',{sec})

thread1=[]
for i in range(5):
    t=threading.Thread(target=name,args=[4])
    t.start()
    thread1.append(t)
for i in thread1:
    t.join()



finish=time.perf_counter()
print("finished in",round(finish-start,2),"sec")



