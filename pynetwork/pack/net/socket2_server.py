'''
Created on 2016. 11. 1.
서버 서비스 유지
'''
import socket
import sys

HOST = ''
PORT = 7878

serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    serversock.bind((HOST, PORT))
    print('서버 서비스중....')
    serversock.listen(5) #동시 최대 접속수
    
    
    while True:
        #수신
        conn, addr = serversock.accept()
        print('client info: ', addr[0], addr[1])
        print(conn.recv(1024).decode()) #암호화 직렬화 패킷단위로 끊어서 간다
        
        #송신
        conn.send(('from server: ' + str(addr[1]) + ' 너도 잘 지내~').encode(encoding='utf_8', errors='strict'))
        
except Exception as e:
    print('server err: ', e)
    sys.exit()
serversock.close()














