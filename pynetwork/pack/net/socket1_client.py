'''
Created on 2016. 11. 1.

'''
from socket import *

clientsock = socket(AF_INET, SOCK_STREAM) #(종류, 유형)
clientsock.connect(('192.168.0.50', 9999))
clientsock.sendall('밥먹으러가자'.encode(encoding='utf_8', errors='strict'))
clientsock.close()