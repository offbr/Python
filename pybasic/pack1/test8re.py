'''
정규표현식 
'''
import re;

ss = '1234 abc가나다ABC_555_6_12345'
print(re.findall(r'123', ss)) #반환타입 list
print(re.findall(r'가나다', ss))
print(re.findall(r'[0-9]', ss))
print(re.findall(r'[0-9]+', ss)) # + = 1이상 / * = 0이상
print(re.findall(r'[0-9]{2,3}', ss)) #2회 또는 3회 반복되는 것

print()
ss = '1234 abc가나다ABC_555_6_mbc air air'
print(re.findall(r'.bc', ss))
print(re.findall(r'^1+', ss)) # ^첫글자 / $마지막글자
print(re.findall(r'[^1].+', ss)) # ^ 대괄호 안에 들어오면 부정
print(re.findall(r'a..', ss)) # a로 시작하는 세글자
print(re.findall(r'air', ss))
print(re.findall(r'air$', ss))

print(re.findall(r'\d', ss)) # \d = 숫자
print(re.findall(r'\d{2}', ss)) # 2회 연속
print(re.findall(r'\d\d\d', ss)) # 3회연속






















