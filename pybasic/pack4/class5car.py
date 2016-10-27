'''
Created on 2016. 10. 26.

클래스의 포함관계 has a
'''
from pack4.class5handle import PohamHandle
class PohamCar:
    turnShow = '정지'
    
    def __init__(self, ownerName):
        self.ownerName = ownerName
        self.handle = PohamHandle() # has a
        
    def TurnHandle(self, q):
        if q > 0 :
            self.turnShow = self.handle.RightTurn(q)
        elif q < 0 :
            self.turnShow = self.handle.LeftTurn(q)
        else:
            self.turnShow = self.handle.StraightTurn(q)
            
tom = PohamCar('tom')
tom.TurnHandle(10)
print(tom.ownerName + '의 회전량은 ' + tom.turnShow + \
       str(tom.handle.quantity))

tom.TurnHandle(-20)
print(tom.ownerName + '의 회전량은 ' + tom.turnShow + \
       str(tom.handle.quantity))

print()
oscar = PohamCar('oscar')
oscar.TurnHandle(10)
oscar.TurnHandle(10)
print(oscar.ownerName + '의 회전량은 ' + oscar.turnShow + \
       str(oscar.handle.quantity))


























