'''
Created on 2016. 10. 27.

with 구문 : close() X
'''
try:
    with open('ftest3.txt', mode='w', encoding='utf-8') as f1:
        f1.write('파이썬으로 문서 저장\n')
        f1.write('with 구문 사용\n')
        f1.write('명시적으로 close() 필요없다 (알아서 해준다)\n')
    print('저장 완료')
    
    print()
    with open('ftest3.txt', mode='r', encoding='utf-8') as f2:
        print(f2.read())
    
    print('\n피클림(집합자료, 복합객체 파일 처리)')
    import pickle
    
    dicdata = {'tom':'111-1111', '길동':'222-2222'}
    listdata = ['마우스', '키보드']
    tupledata = (dicdata, listdata) #복합객체
    
    with open('hello.dat', 'wb') as f3:
        pickle.dump(tupledata, f3) #pickle.dump(대상, 파일객체)
        pickle.dump(listdata, f3)
    print('파일 저장 성공')
    
    print('읽기-------') 
    with open('hello.dat', 'rb') as f4:
        a, b = pickle.load(f4)
        print(a)
        print(b)
        print()
        c = pickle.load(f4)
        print(c)
    


except Exception as e:
    print('에러:', e)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
