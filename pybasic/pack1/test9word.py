'''
Created on 2016. 10. 24.

word count
'''

# ------- word count
import re

ss = '''밥 딜런이 지난 13일 노벨 문학상을 수상하고도 무대응으로 일관하자 상을 주관하는 스웨덴 한림원이 발끈했다. 
스웨덴 작가이자 한림원 노벨 문학상 선정위원인 페르 베스트베리가 공영 SVT방송에서 “딜런이 무례하고 오만하다”고 말했다고 AFP통신이 22일(현지시간) 보도했다.
딜런은 한림원이 전화를 해도 받지 않고, 수상 소감을 포함해 어떤 입장도 내놓지 않고 있다.
매년 12월 10일은 노벨상 수상자가 스톡홀름으로 초대돼 스웨덴 국왕 칼 구스타프 16세에게 상을 받고 소감을 밝힌다. 
그러나 딜런의 시상식 참석 여부는 아직까지 불투명하다. 베스트베리는 “전례 없는 경우”라고 말했다. 수상 거부설도 나온다. 
딜런은 노벨 문학상 수상자가 발표되는 날 미국 라스베이거스에서 공연하면서 마지막 곡으로 ‘왜 나를 지금 바꾸려고 하나요(Why try to change me now)’를 불러 거부설에 불을 지폈다.
공식 홈페이지에는 ‘노벨 문학상 수상자(winner of the Nobel prize in literature)’라는 문구가 한때 있었으나 삭제됐다.
''' 
ss2 = re.sub(r'[^가-힣\s]', '', ss) #영문 제외
print(ss2)

ss3 = ss2.split(' ')
print(ss3)

cou = {} #튜플타입
for i in ss3:
    if i in cou:
        cou[i] += 1
    else:
        cou[i] = 1
print(cou)        

print('\n사전형 자료 처리 예')
from time import localtime
print(localtime())
act = {6:'잠', 9:'아침먹고 출근', 18:'일하자', 20:'연장', 24:'휴식'}
print(act)
hour = localtime().tm_hour
print(hour)
print(sorted(act.keys()))

for act_time in sorted(act.keys()):
    if hour < act_time:
        print(act[act_time])
        break
    else:
        print("뭐야")













