'''
Created on 2016. 10. 24.

Closure : scope에 제약을 받지 않는 변수를 포함한 코드블럭
'''
from _ast import Nonlocal

#함수명은 객체의 주소를 갖는다.
def Times(a, b):
    c = a * b
    return c

print(Times(2, 3))
#print(c) #클로저를 쓰면 함수내의 변수를 참조할 수 있다
kbs = Times
print(kbs(2, 3))

del Times #함수의 이름을 삭제
#print(Times(2, 3)) #NameError: name 'Times' is not defined
print(kbs(2, 3))
mbc = kbs
print(mbc(3, 4))

print('\n클로저 X')
def out():
    count = 0
    def inn():
        nonlocal count
        count += 1
        return count
    print(inn())

out()
out()

#print(count) #NameError: name 'count' is not defined

print('\n클로저 O')
def outer():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner #이게 클로저 : 내부함수를 반환 (주소)

print(outer()) #<function outer.<locals>.inner at 0x1036040d0> #주소값
ytn = outer()
print(ytn())
print(ytn())
print(ytn())

print()
jtbc = outer()
print(jtbc())

print()
j = iter(['tom', 'oscar'])
print(j)
print(next(j))
print(next(j))

#사용 예
print('수량 * 단가 * 세금 결과 출력')
def outer2(tax):
    def inner2(su, dan):
        amount = su * dan * tax
        return su * dan - amount
    return inner2

jan_money = outer2(float(0.1))
result = jan_money(5, 10000)
print(result)
result = jan_money(3, 5000)
print(result)

print()
feb_money = outer2(float(0.05))
result = feb_money(5, 10000)
print(result)














