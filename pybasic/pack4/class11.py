'''
Created on 2016. 10. 26.

추상 클래스
'''
from abc import abstractmethod, ABCMeta
from test.pickletester import metaclass
class AbstractClass(metaclass=ABCMeta): #추상 클레스
    
    @abstractmethod
    def abcMethod(self): #추상메소드
        pass
    
    def normalMethod(self):
        print('일반메소드')
        
#abs = AbstractClass() #TypeError: Can't instantiate abstract class AbstractClass with abstract methods abcMethod
class Child1(AbstractClass):
    name = '난 child1'

    def abcMethod(self):
        print('추상 메소드를 재정의')
    
c1 = Child1()
print(c1.name)
c1.abcMethod()
c1.normalMethod()












