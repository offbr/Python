'''
Created on 2016. 11. 1.

thread 
'''
'''
from subprocess import *

#Popen("/Applications/Calculator.app")
print("다음")
#call("/Applications/Calculator.app")
print("다음2")
'''

import threading, time

def run(id):
    for i in range(1, 11):
        print('id={} --> {}'.format(id, i))
        time.sleep(0.5)
        
#run(1) #thread X
#run(2)

# thread O
th1 = threading.Thread(target=run, args=(1,)) #튜플타입
th2 = threading.Thread(target=run, args=(2,)) #튜플타입
th1.start()
th2.start()
th1.join()
th2.join()
print("종료")






































