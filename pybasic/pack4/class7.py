'''
Created on 2016. 10. 26.

상속 is a     클래스 aa(상속클래스명):
'''
class Animal:
    def move(self):
        print('움직이는 생물')

class Dog(Animal):  # is a
    def my(self):
        print('나는 개야~')
        
dog1 = Dog()
dog1.my()
dog1.move()

print()
class Horse(Animal):
    pass

horse1 = Horse()
horse1.move()








