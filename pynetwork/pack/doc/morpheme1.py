'''
Created on 2016. 11. 2.

형태소
'''
from konlpy.tag import Kkma
from konlpy.utils import pprint
kkma = Kkma()
pprint(kkma.sentences('여러분, 안녕하세요. 반갑습니다.'))
print()
pprint(kkma.nouns(u'오늘 폭염이 주춤했지만 일부지방은 폭염 특보 속에 35도 안팎의 찜통더위가 기승을 부렸는데요.자세한 날씨, YTN 중계차 연결해 알아보겠습니다.'))
print()
pprint(kkma.pos(u'오류보고는 실행환경, 에러메세지와 함께'))