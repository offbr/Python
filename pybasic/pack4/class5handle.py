'''
Created on 2016. 10. 26.

다른 클래스에서 참조하기 위한 클래스
'''
class PohamHandle:
    quantity = 0
    
    def LeftTurn(self, quantity):
        self.quantity = quantity
        return '좌회전'
    
    def RightTurn(self, quantity):
        self.quantity = quantity
        return '우회전'
    
    def StraightTurn(self, quantity):
        self.quantity = quantity
        return '직진'