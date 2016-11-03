'''
Created on 2016. 11. 1.

thread의 활성화, 비활성화
'''
import threading, time

bread_plate = 0 #공유자원
cv= threading.Condition() #lock를 위한 조건변수

class Maker(threading.Thread):
    def run(self):
        global bread_plate
        for i in range(30):
            cv.acquire() #공유자원 충돌방지
            while bread_plate >= 10:
                print('빵 생산 초과로 대기')
                cv.wait() # 스레드 비활성화
                
            bread_plate += 1
            print('빵 생산', bread_plate)
            cv.notify() #스레드 활성화
            cv.release()
            time.sleep(0.5)
                
class Consumer(threading.Thread):
    def run(self):
        global bread_plate
        for i in range(30):
            cv.acquire() #공유자원 충돌방지
            while bread_plate < 1 :
                print('빵이 없어서 기다림')
                cv.wait() # 스레드 비활성화
                
            bread_plate -= 1
            print('빵 소비', bread_plate)
            cv.notify() #스레드 활성화
            cv.release()
            time.sleep(0.5)
                
mak = []; con = []

for i in range(5): #생산자 수
     mak.append(Maker())
    
for i in range(5): #소비자 수
     con.append(Consumer())


for th1 in mak:
    th1.start()

for th2 in con:
    th2.start()

for th1 in mak:
    th1.join()

for th2 in con:
    th2.join()
    
print('오늘 장사 끝')




















