'''
Created on 2016. 10. 27.

예외처리
'''

def divide(a, b):
    return a / b

print('뭔가를 하다가...')
'''
c = divide(5, 0) #ZeroDivisionError: division by zero
print(c)
'''
try:
    c = divide(5, 2)
    print(c)
    
    aa = [1, 2]
    print(aa[1])
    
    f = open(r'/user/aa.txt')
    
except ZeroDivisionError:
    print('두번째 숫자는 0을 주지 마세요')
except IndexError as e:
    print('참조 오류', e)
except Exception as e: 
    print('에러:', e)   
finally:
    print('에러와 상관없이 수행')    

print()

def PositiveDivide(a, b):
    if b < 0 :
        raise NegativeDivisionError(b)
    return a / b

class NegativeDivisionError(Exception):
    def __init__(self, value):
        self.value = value

print('에러처리 2')
try:
    result = PositiveDivide(10, 2)
    #result = PositiveDivide(10, -2)
    #result = PositiveDivide(10, 0)
    print(result)
except NegativeDivisionError as e: 
    print('err : second arg is ', e.value)
except ZeroDivisionError as e:
    print('err : ', e.args[0])
except Exception as e:
    print(e)
    print(e.args[1])    
    
    
    
    
    
    
    
    
    
    
print('종료')












