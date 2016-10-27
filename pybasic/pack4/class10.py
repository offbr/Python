'''
Created on 2016. 10. 26.

다중 상속 : 순서가 중요
'''
class Tiger:
    data = '호랑이 세상'
    
    def Cry(self):
        print('호랑이 어흥!!!')
        
    def Eat(self):
        print('맹수는 고기를 먹음')

class Lion:
    def Cry(self):
        print('사자는 으르렁!!!!!!')
    
    def Hobby(self):
        print('백수의 왕은 낮잠이 취미')
        
class Liger1(Tiger, Lion): #다중 상속
    pass 

a1 = Liger1()
a1.Cry() #멤버를 찾아가는 순서 Liger1 > Tiger > Lion
a1.Eat()
a1.Hobby()
print(a1.data)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        