'''
Created on 2016. 10. 19.
여러줄 주석
'''

"""
여러줄 주석
"""

# 한줄 주석

a = 3 #이거 권장 a=3
print(a)
print(id(a), id(3), type(a))
a = b = c = 10
print(a, b, c)
a, b, c = 7, "안녕", '반가워' #문자는 없다 문자열만 있다.
print(a, b, c)

total = 2 + \
3 * 4
print(total)

print('a', end=' ') #end=' ' 같은 라인
print('b')

print()

print(format(123.45678, '10.3f'))  #123.457
print(format(123.45678, '10.3'))   #1.23e+02 과학적 표기법으로 출력.
print(format(123, '10d'))          #123  정수에 대한 전체 자리수 지정.
           
print('서식에 의한 자료 출력 %s %d %f'%('문자열', 5, 23.4))

print('이름:{0}, 가격:{1}'.format('마우스', 5000)) #순서를 적지 않으면 0부터 맵핑

print('이름:{0}, 가격:{1} 이름:{0}, 가격:{1}, 가격:{1}'.format('마우스', 5000))

print(format(1.5678, '10.3f'))

print()

print('나는 나이가 %d 이다.'%23)
print('나는 나이가 %s 이다.'%'스물셋')
print('나는 나이가 %d 이고 이름은 %s이다.'%(23, '홍길동'))
print('나는 나이가 %s 이고 이름은 %s이다.'%(23, '홍길동'))
print('나는 키가 %f이고, 에너지가 %d%%.'%(177.7, 100))
print('이름은 {0}, 나이는 {1}'.format('한국인', 33))
print('이름은 {}, 나이는 {}'.format('신선해', 33))
print('이름은 {1}, 나이는 {0}'.format(34, '강나루'))









