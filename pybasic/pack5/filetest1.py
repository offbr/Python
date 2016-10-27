'''
Created on 2016. 10. 27.

file i/o
'''
import os

try:
    print('파일 읽기')
    print(os.getcwd())
    f1 = open(os.getcwd() + r'/ftest.txt', encoding='utf-8')
    print(f1)
    print(f1.read(), end = ' ')
    f1.close()
    
    print('\n파일 저장 -----')
    f2 = open('ftest2.txt', mode='w', encoding='utf-8')
    f2.write('무궁화 삼천리 화려강산 \n')
    f2.write('대한사람 대한으로 \n')
    f2.write('길이 보전하세 \n')
    f2.close()
    print('저장 성공')
    
    print('\n파일 추가')
    f2 = open('ftest2.txt', mode='a', encoding='utf-8')
    f2.write('동해물과 백두산이 \n')
    f2.write('마르고 닳도록 \n')
    f2.close()
    print('추가 성공')
    
    
    print('파일 읽기2')
    f3 = open(os.getcwd() + r'/ftest2.txt', encoding='utf-8')
    print(f3.read(), end = ' ')
    f3.close()
    
    print()
    f3 = open(os.getcwd() + r'/ftest2.txt', encoding='utf-8')
    print(f3.readline())
    print(f3.readline(1), f3.readline(3))
    f3.close()
    
    print('파일 읽기3 --슬라이싱--')
    f3 = open(os.getcwd() + r'/ftest2.txt', encoding='utf-8')
    lines = f3.readlines()
    print(lines)
    print(lines[1:])
    print(lines[2:5:2])
    f3.close
    
    print()
    import sys
    sys.stdout.writelines(lines[3:])
    print()
    sys.stdout.writelines(lines[1:3])
    
    print('\n파일 목록')
    import glob
    print(glob.glob('*'))
    print(glob.glob('*.txt'))
    print(glob.glob('??????.txt'))
    
except Exception as e:
    print('err: ', e)







































