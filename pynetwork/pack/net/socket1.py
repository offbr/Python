'''
Created on 2016. 11. 1.

socket : TCP/IP 기반 
'''
import socket

print(socket.getservbyname('http', 'tcp')) #포트번호 80번
print(socket.getservbyname('telnet', 'tcp')) #포트번호 23번
print(socket.getservbyname('ftp', 'tcp')) #포트번호 21번

print(socket.getaddrinfo("www.naver.com", 80, proto=socket.SOL_TCP))

