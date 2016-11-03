'''
Created on 2016. 11. 1.

'''
from socket import *

clientsock = socket(AF_INET, SOCK_STREAM) #(종류, 유형)
clientsock.connect(('', 7878))
clientsock.sendall('오뎅에 사케 고고'.encode(encoding='utf_8', errors='strict'))
re_mes = clientsock.recv(1024).decode()

print('수신자료는 ' + str(re_mes)) 
clientsock.close()