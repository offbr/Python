'''
집합 자료형 - str, list, tuple, dict
'''
#str : 문자들을 표현, 따옴표를 두름, 순서o, 수정x, 슬라이싱 가능

a = 'Hello'
print(a, id(a))
a = '안녕'
print(a, id(a), a[0])
#a[0] = '가'  #TypeError: 'str' object does not support item assignment
ss = "대한 민국 만세 만세"
print(ss)
print(ss[0], ss[2:], ss[:3])
print(ss[0:3], ss[-3:-1], ss[0:5:2])
print(ss.count('인'), len(ss))

ss2 = ss.split(sep=' ') #자르기
print(ss2)
ss3 = ' '.join(ss2) #붙이기
print(ss3)

