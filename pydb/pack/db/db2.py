'''
Created on 2016. 10. 28.

원격DB - Maria DB
''' 
import MySQLdb

import sys
print(sys.path)



# conn = MySQLdb.connect(host = 'localhost', user = 'root', passwd='123', db='test')
# print(conn)
# conn.close

config = {
    'host' : '127.0.0.1',
    'user' : 'root',
    'password' : '',
    'database' : 'test',
    'port' : 3306,
    'use_unicode' : True,
    'charset' : 'utf8'
    }

try:
    conn = MySQLdb.connect(**config)
    cursor = conn.cursor()
    
    #자료 추가
#     sql = "insert into sangdata values(108, '신상1', 3, 5000)"
#     cursor.execute(sql)
    
    '''
    sql = "insert into sangdata values (%s,%s,%s,%s)"       #local DB일 경우에는 인자값을 ?로, remote DB일 경우에는 %s
    sql_data = ('10', '새상품', 10, 2000)
    cursor.execute(sql, sql_data)
    conn.commit()
    '''
    
    #자료 수정
    sql = "update sangdata set sang = %s, su = %s, dan = %s where code = %s"
    sql_data = ('초코바', 50, 2200, '102')
    cursor.execute(sql, sql_data)
    conn.commit()

    
    #자료 삭제
    code = '104'
    #sql = "delete from sangdata where code = " + code       #이런 방법도 가능 (그러나 권장하지 않는다)
    #sql = "delete from sangdata where code = {0}".format(code)
    sql = "delete from sangdata where code = %s"       
    cursor.execute(sql, (code,))        #code는 tuple type으로 들어가야 한다
    conn.commit()
    
    #자료 읽기
    sql = "select * from sangdata"
    
    
    #방법1
    cursor.execute(sql)
    for data in cursor.fetchall():
        #print(data)
        print('%s %s %s %s'%data)
    
    #방법2
    print()
    cursor.execute(sql)
    for r in cursor:
        #print(r)
        print(r[0], r[1], r[2], r[3])
    
    #방법3
    print()
    cursor.execute(sql)
    for(code, sang, su, dan) in cursor:
        print(code, sang, su, dan)
    
    
    #방법3-1 단순한 변수명이다.
    print()
    cursor.execute(sql)
    for(a, b, c, d) in cursor:
        print(a, b, c, d)
    
except Exception as e:
    print('에러: ' + str(e))
    
finally:
    cursor.close()
    conn.close()
    
    
    
