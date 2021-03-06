'''
Created on 2016. 10. 25.

사용자 정의 모듈
'''
print('사용자 정의 모듈 읽기')
import pack3.mymod1

print(dir(pack3.mymod1)) # 가지고 있는 변수 및 함수
print(pack3.mymod1.__file__) #경로
print(pack3.mymod1.__name__)

print('mymod1 모듈의 멤버 읽기')
a = 10, 20, 30, 40
b = [1, 2, 3, 4]
pack3.mymod1.dataList(a, b)

if __name__ == '__main__': #필수 메인모듈 판단.
        print('나는 최상위 모듈~~')

print()
from pack3 import mymod1
print(mymod1.myage)
mymod1.kbs()

print()
from pack3.mymod1 import kbs, mbc, sbs, myage
print(myage)
sbs()
kbs()
mbc()

print('\n 같은 package에서 모듈 호출할 때와 동일') #파이썬은 무조건 public
from etc.mymod2 import Hap, Cha
print(Hap(5, 3))
print(Cha(5, 3))

print('\n Path가 설정된 폴더의 모듈 읽기')
import mymod3 #/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5
aa = mymod3.Gop(4, 3)
print(aa)

from mymod3 import Gop
print(Gop(3, 7))

print('\n 전혀 다른 폴더의 모듈 읽기')
#방법 1 : Path에 폴더를 추가
#방법 2 : 
import sys #권장방법은 아니다.
sys.path.append(r'/Library/Frameworks/Python.framework/Versions/3.5')
#import mymod4 #이클립스 에러...
#print('나누기는 ', mymod4.Nanu(10, 2))


#그래픽
from turtle import *
p = Pen()
p.color('red', 'yellow')
p.begin_fill()
while True:
    p.forward(200)
    p.left(170)
    if abs(p.pos()) < 1:
        break
p.end_fill()

input()


















