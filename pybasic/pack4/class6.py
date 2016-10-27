'''
Created on 2016. 10. 26.

클래스의 포함 has a
'''
class Robot:
    name = '태권v'
    energy = 80
    
    def attack(self):
        return '발차기'
    
print('일반 작업 도중에...')
robot = Robot() #로봇타입의 객체를 만들어서 넘겨준다
robot.name = '호빵맨' #원형클래스가 아니라 로봇타입의 인스턴스를 바꿨다
print('이 름:', robot.name)
print('에너지:', robot.energy)
print('필살기:', robot.attack())

print()
robot2 = Robot #주소를 치환
robot2.name = '아이언맨' #원형클래스를 변경
print('이 름:', robot2.name)
print('에너지:', robot2.energy)
print('필살기:', robot2.attack(robot2))

print()
print(robot.name)


print('프로그램 종료')


















