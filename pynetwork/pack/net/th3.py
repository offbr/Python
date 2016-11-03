'''
Created on 2016. 11. 1.

thread 상속
'''
import threading
class MyThread(threading.Thread):
    def run(self):
        for i in range(1, 11):
            print('id:{} --> {}'.format(self.getName(), i))
            
ths = []
for i in range(2):
    th = MyThread()
    th.start()
    ths.append(th)

for th in ths:
    th.join()
    
print('Bye')