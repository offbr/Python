'''
Created on 2016. 10. 24.
rage() : 범위 내의 집합자료 반환
'''
print(list(range(1, 6)))
print(list(range(0, 11, 2))) #등차수열
print(list(range(-10,-100, -20)))
print(set(range(1, 6)))
print(tuple(range(1, 6)))
print(list(range(10))) #초기치 안 줄 경우 0 부터 시작

print()
for i in range(6):
    print(i, end= ' ')
    
print()

# 1 ~ 10 까지의 숫자의 합?
a = 0;
for i in range(11):
    a += i    
print(a)    

# 2 - 9 구구단 출력
for i in range(2, 10):
    for j in range(1, 10):
            print(i , " * " , j , " = " , (i*j), end= ' ')
    print()
# 1 ~ 100 까지의 3의 배수이면서 5의 배수인 숫자의 합은 ?
a = 0; 
for i in range(100):
    if i % 3 == 0 and i % 5 == 0:
        a += i
print(a)

print()

li = ['a', 'b', 'c']
for k, d in enumerate(li):
    print(k, d)




















