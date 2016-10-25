'''
Created on 2016. 10. 25.

재귀함수 : 함수가 자신을 호출 - 반복처리
'''

def Countdown(n):
    if n == 0:
        print('처리완료')
    else:
        print(n, end= ' ')
        Countdown(n - 1) #이게 재귀

Countdown(5)
print()
print('다음 작업')