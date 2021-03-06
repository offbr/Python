'''
Created on 2016. 10. 26.

상속 is a
'''
class Person:
    say = '난 사람이야~'
    age = 20
    __weight = 77 # __ private
    
    def __init__(self, age):
        print('Person 생성자')
        self.age = age #self = Person
        
    def printInfo(self):
        print('나이:{}, 이야기:{}'.format(self.age, self.say))
        
    def hello(self):
        print('안녕')
        print('몸무게:', self.__weight)
        
    @staticmethod
    def sbs(tel):
        print('sbs-static method : 현재 클래스 소속', tel)
        #print(self.say)
         
    @classmethod
    def kbs(cls):
        print('kbs-class method', cls.say, cls.__weight, cls.age)
        
    
class Employee(Person):
    say = '난 일하는 동물'
    subject = '근로자'
    
    def __init__(self):
        print('Employee 생성자')
        
    def printInfo(self):
        print('Employee 메소드')
    
    def ePrintInfo(self):
        self.printInfo()
        super().printInfo()
        print(self.say, super().say)
        self.hello()
        #print('몸무게:', super().__weight) # AttributeError: 'Employee' object has no attribute '_Employee__weight'
        
e = Employee() #생성자는 명시적으로 부르지 않으면 생성되지 않는다.
print(e.say, e.age, e.subject)       
e.printInfo()
print()
e.ePrintInfo()

print('**' * 20)

print()
#e.sbs('222-2222') #비권장
Person.sbs('111-1111')

print()
#e.kbs() #비권장
Person.kbs()

print('**' * 20)

class Worker(Person):
    def __init__(self, age):
        print('Worker 생성자')
        super().__init__(age) #부모 클래스의 생성자 호출 : Bound method call
    
    def printInfo(self):
        print('Worker의 printInfo')    
        
    def wPrintInfo(self):
        super().printInfo()
        
w = Worker(25)        
print(w.say, w.age)
print(w.__dict__)
w.wPrintInfo()

print('^^' * 20)

class Programmer(Worker):
    def __init__(self, age):
        print('Programmer 생성자')
        Worker.__init__(self, age) #부모 클래스의 생성자 호출 : UnBound method call
    
pr = Programmer(33)
print(pr.say, pr.age)    
pr.printInfo()

print('\n\n class type')
a = 10
print(type(a))
print(type(pr))
print(Programmer.__bases__) #부모확인
print(Person.__bases__) #부모확인 #object















