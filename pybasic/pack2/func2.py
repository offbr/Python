'''
Created on 2016. 10. 24.

변수의 생존 범위 Local > Enclosing function > Global > built-in
'''
player = '전국대표' #전역변수

def FuncSoccer():
    name = '홍길동' #지역변수
    player = '동네대표'
    print(name, player)

FuncSoccer()
print(player)
#print(name) #NameError: name 'name' is not defined

print()

a = 10; b = 20; c = 30
print('a:{}, b:{}, c:{}'.format(a, b, c))

def Foo():
    a = 40
    b = 50
    def Bar(): #내부함수
        #c = 60
        global c
        nonlocal b
        print('a:{}, b:{}, c:{}'.format(a, b, c))
        c = 60 #순서상 global이라 명시 해줘야 한다(나중에 다시 명시 해줬기 떄문에 값을 못 찾는다) UnboundLocalError: local variable 'c' referenced before assignment
        b = 70
        
    Bar()
    a = 80
    
Foo()        
print('a:{}, b:{}, c:{}'.format(a, b, c))

print()
g = 1
def func():
    global g
    a = g # 나중에 g를 다시 명시했기 때문에 넘겨야할 값을 못찾는 것. (global b 명시) UnboundLocalError: local variable 'g' referenced before assignment
    g = 2  
    return a + g

print(func())
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        