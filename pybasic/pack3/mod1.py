'''
Created on 2016. 10. 25.

module : 응용프로그램의 실행 단위, 자원의 재활용을 목적
            표준모듈, 제 3자 모듈, 사용자 정의 모듈
'''
print('뭔가를 하다가')
import sys
print('모듈 경로:', sys.path)
#sys.exit()

import math
print(math.pi)
print(math.sin(30))
print(math.cos(30))
print(math.degrees(30))
print(math.sin(math.radians(30)))

import calendar
calendar.setfirstweekday(6) #달력의 주 시작요일 설정
calendar.prmonth(2016, 10)

import random
print(random.random())
print(random.randrange(1, 10))

from random import random, randrange
print(random())
print(randrange(1, 10))

from random import * # 파이썬은 * 을 걸면 관련 함수들이 모두 메모리에 올라오므로 권장방법이 아니다. (자바는 *을 걸어도 관련 메소드만 올라옴)
print(random())

print("프로그램 종료")
















