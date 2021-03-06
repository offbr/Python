'''
Created on 2016. 10. 28.

db 연동 프로그래밍 - sqlite3
'''
import sqlite3
print(sqlite3.sqlite_version_info)

print()
#conn = sqlite3.connect("example.db")
conn = sqlite3.connect(":memory:") #휘발성 - 테스트용

try:
    c= conn.cursor()
    
    c.execute("create table if not exists friends(name text, phone text, addr text)") #없으면 생성
    
    c.execute("insert into friends(name, phone, addr) values('한국인', '000-0000', '역삼1동')")
    c.execute("insert into friends values('지구인', '111-1111', '지구1동')")
    c.execute("insert into friends values(?,?,?)",('우주인', '222-2222', '은하계1호'))
    inputdata = ('목성인','333-3333', '목성1동')
    c.execute("insert into friends values(?,?,?)", inputdata)
    conn.commit()
    
    c.execute("select * from friends")
    print(c.fetchone()) #튜플타입
    print(c.fetchall()) #리스트타입 안에 튜플타입 
    
    print()
    c.execute("select * from friends") #위에서 포인터의 이동이 끝났기 때문에 다시 읽어줘야 한다.
    for r in c:
        print(r[0] + ' ' + r[1] + ' ' + r[2])
    
    
    
    
    
except Exception as e:
    print('err: ' + str(e))
    conn.rollback()
finally:
    conn.close()    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    