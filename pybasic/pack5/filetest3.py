'''
Created on 2016. 10. 27.

동이름으로 우편주소 찾기
'''
try:
    dong = input('동이름을 입력:')
    #print(dong)
    
    with open(r'zipcode.txt', mode='r', encoding='euc-kr') as f:
        line = f.readline()
       
        #print(line)
        while line:
            #lines = line.split('\t')
            lines = line.split(chr(9))
            #print(lines)
            if lines[3].startswith(dong):
                #print(lines)
                print('[' + lines[0] + ']' + lines[1] + ' ' + \
                      lines[2] + ' ' + lines[3] + ' ' + lines[4])
            
            line = f.readline()
             


except Exception as e:
    print('err :', e)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    