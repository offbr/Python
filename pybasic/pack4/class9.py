'''
Created on 2016. 10. 26.

메소드 오버라이드 
'''
class Parent:
    def printInfo(self):
        pass
    
class Child1(Parent):
    def printInfo(self):
        print('Child1에서 오버라이딩')

class Child2(Parent):
    def printInfo(self):
        print('Child2에서 overriding')
        print('부모 메소드를 재정의')
    
    def aa(self):
        print('aa method')

c1 = Child1()
c1.printInfo()
print()
c2 = Child2()
c2.printInfo()

print('\n다형성------')
par = Parent
par = c1
par.printInfo()
print()
par = c2
par.printInfo()

print() 
my = c1 #부모객체가 아니라 일반 변수에 넘겨도 된다 #함수형 언어는 느슨하다.
my.printInfo()
print()
my = c2
my.printInfo()
my.aa()

print()
plist = [c1, c2]
for i in plist:
    i.printInfo()
































