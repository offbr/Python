'''
Created on 2016. 10. 25.
'''
class Car:
    handle = 0;
    speed = 0;
    
    def __init__(self, name, speed):
        self.speed  = speed
        self.name  = name
    
    def showData(self):
        km = '킬로미터'
        msg = '속도: ' + str(self.speed) + km
        return msg
    
print(Car.handle)

print()
car1 = Car('tom', 10)
print(car1.handle,car1.name, car1.speed)
car1.color = '검정'
#print(Car.color)
print(car1.color)

print('**' * 10)
car2 = Car('john', 20)
#print(car2.color)

print(id(Car), id(car1), id(car2))
print()

car1.speed = 10
car2.speed = 20

print(car1.showData())
print(car2.showData())

Car.handle = 1
car1.handle = 2
#자신의 이름공간 안에서 찾는 값이 없으면 원형클래스의 값을 참조한다.
print(car1.handle)
print(car2.handle)

print(car1.__dict__)











