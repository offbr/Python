'''
Created on 2016. 10. 25.

class
'''
#클래스는 header(멤버변수)와 body(클래스,패스)영역으로 구성된다
print('클래스는 모듈의 멤버 중 하나')
class TestClass: #클래스의 이름만큼은 대문자로 쓴다.
    aa = 1 #멤버변수 -- prototype
    
    def __init__(self): #파이썬은 오버로딩x 접근지정자x 오버라이딩o
        print('생성자')
        
    def __del__(self):
        print('소멸자')
    
    def printMessage(self):
        name = '한국인' #지역변수
        print(name)
        print(self.aa)
        
TestClass() #생성자 호출
print(TestClass.aa)
print(TestClass, type(TestClass), id(TestClass))
#TestClass.printMessage() #TypeError: printMessage() missing 1 required positional argument: 'self'

print()
test = TestClass()
print(test.aa, test)
print(id(test))

print('--------')
test.printMessage() #Bound method call
TestClass.printMessage(test) #UnBound method call
print('--------')

print(isinstance(test, TestClass)) #맞으면 t 틀리면 f
print(type(1))
print(type(test))

print('종료')
















































