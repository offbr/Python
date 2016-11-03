'''
Created on 2016. 11. 1.

echo server : 클라이언트의 요청에 따라 반응 / 대체적으로 에코서버 / node는 동적
'''
from socket import *

serversock = socket(AF_INET, SOCK_STREAM) #(종류, 유형)
serversock.bind(('127.0.0.1', 9999)) #반드시 바인드는 튜플타입
serversock.listen(1) #1 ~ 5
print('server service start...')

conn, addr = serversock.accept() #연결대기
print('client addr : ', addr)
print('from client message: ', conn.recv(1024).decode())
conn.close()
serversock.close()