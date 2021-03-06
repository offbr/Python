'''
Created on 2016. 10. 26.

문제 1
'''
from abc import abstractmethod, ABCMeta
from test.pickletester import metaclass
class Employee(metaclass=ABCMeta):
    irum = ''; nai = 0
    
    @abstractmethod
    def pay(self):
        pass 

    @abstractmethod
    def data_print(self):
        pass 

    def display(self):
        print(self.irum, self.age)
        
class Temporany(Employee):
    ilsu=0; ildang=0
    
    def __init__(self, irum, nai, ilsu, ildang):
        self.irum = irum
        self.nai = nai
        self.ilsu = ilsu
        self.ildang = ildang
        self.data_print()
        self.pay()
    
    def pay(self):
        print('월급:',self.ilsu * self.ildang)
        
    def data_print(self):
        print('이름:',self.irum,' 나이:',self.nai, end =' ')
            
t = Temporany('홍길동', 25, 10, 15000)

class Regular(Employee):
    salary = 0
    
    def __init__(self, irum, nai, salary):
        self.irum = irum
        self.nai = nai
        self.salary = salary
        self.data_print()
        self.pay()
        
        
    def pay(self):
        print('월급',self.salary)
    
    def data_print(self):
        print('이름:',self.irum,' 나이:',self.nai, end = ' ')
    
r = Regular('한국인','27','35000')

class Salesrnan(Regular):
    sales = 0; commission = 0;
    
    def __init__(self, irum, nai, salary, sales, commission):
        self.irum = irum
        self.nai = nai
        self.salary = salary
        self.sales = sales
        self.commission = commission
        self.data_print()
        self.pay()
    
    def pay(self):
        print('수령액', self.salary + (self.sales * self.commission))
    
    
s = Salesrnan('손오공',29,1200000,5000000,0.25)    
    
    
    
    
    
    
    
        
        

