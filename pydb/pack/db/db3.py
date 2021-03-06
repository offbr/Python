'''
Created on 2016. 10. 31.

부서번호 입력 후 직원자료 읽
'''
import MySQLdb
import sys

config = {
    'host' : '127.0.0.1',
    'user' : 'root',
    'password' : '',
    'database' : 'test',
    'port' : 3306,
    'charset' : 'utf8',
    'use_unicode' : True
    }

try:
    conn = MySQLdb.connect(**config)
    cursor = conn.cursor()
    
    buser_no = input('부서번호 입력: ')
    sql = '''
        select sawon_no, sawon_name, buser_num, sawon_jik
        from sawon
        where buser_num={}
    '''.format(buser_no)
    
    cursor.execute(sql)
    datas = cursor.fetchall()
    
    if len(datas) == 0:
        print(buser_no + '번은 없는 부서 입니다')
        sys.exit()
        
    for d in datas:
        print(d[0], d[1], d[2], d[3]) 
    
    print('인원수 : ' + str(len(datas)))
       
except Exception as e:
    print('에러: ' + str(e))
        
finally:
    cursor.close()
    conn.close()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    