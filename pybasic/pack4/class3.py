'''
Created on 2016. 10. 25.
'''
kor = 100 #전역변수

def abc():
    print('함수')

class My:
    kor = 90 #멤버변수
    def abc(self):
        print('메소드')
        
    def show(self):
        ##kor = 70 #지역변수
        print(kor)
        print(self.kor)
        self.abc()
        abc()
        
m = My()
m.show()

print('^^' * 20)


class Our:
    a = 1
    
print(Our.a)

print()
our1 = Our()
print(our1.a)

print()
our1.a = 2
print(our1.a)
    
print()
our2 = Our()
print(our2.a)
our2.b = 3
print(our2.b)

#print(our1.b)
#print(Our.b)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    