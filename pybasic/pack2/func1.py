'''
Created on 2016. 10. 24.

함수 => def 함수명(arg...) : 
'''
#내장 함수
from test.pyclbr_input import Other
print(sum([3 + 5]), sum({3, 5}), sum((3, 5)))
print(int(1.7), float(7), str(5) + '오')
print(round(1.7), round(1.4))

import math
print(math.ceil(1.2), math.ceil(1.7))
print(math.floor(1.2), math.floor(1.7))

a = 10 
b = eval('a + 5') #문자열을 수식을 만들어 준다.
print(b)

print()
b_list = [True, False]
print(all(b_list))
print(any(b_list))

b_list2 = [1,2,3,4,5,6,7]
print(all(a < 10 for a in b_list2)) #모든 숫자가 10 미만이야?
print(any(a < 10 for a in b_list2)) #모든 숫자가 10 미만이 하나라도 있어?

x = [10, 20, 30]; y = ['a', 'b']
for i in zip(x, y): #매칭
    print(i)

print('**' * 20)
#사용자 정의 함수
def DoFunc1():
    print('DoFunc1 Process')

def DoFunc2(arg1, arg2):
    print('DoFunc2 Process')
    aa = arg1 + arg2
    #print('aa : ' , aa) #리턴값 파이썬은 리턴을 명시 하지 않아도 값을 리턴한다. 
    #return None = #return
    return aa

print('어쩌구 저쩌구...')
DoFunc1()
print()
DoFunc1()

#OtherFunc = DoFunc1() #실행 결과를 줌
OtherFunc = DoFunc1 #주소를 치환
OtherFunc()
print(id(OtherFunc), id(DoFunc1))
print('현재 파일의 객체 목록:', globals())

print()
DoFunc2(10, 20)
DoFunc2("대한", "민국")
#DoFunc2(3) #TypeError: DoFunc2() missing 1 required positional argument: 'arg2'
#DoFunc2(3, 4, 5) #TypeError: DoFunc2() takes 2 positional arguments but 3 were given

print(DoFunc2(10, 20)) 
result = DoFunc2(10, 20)
print(result) 

def Area_tri(a, b):
    c = a * b / 2
    Area_tri_print(c) #함수는 함수를 부르거나 쓸 수 있다.
    
def Area_tri_print(c):
    print('삼각형의 면적은 ', c)
    
Area_tri(10, 20)

def swap(a, b):
    return b, a


a = 1; b = 2
a, b = swap(a, b) # 함수는 반환값이 복수일 수 있다.
print(a, b)



print('종료')











