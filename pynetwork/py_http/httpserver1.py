'''
Created on 2016. 11. 3.

Http server를 운영
'''
from http.server import SimpleHTTPRequestHandler, HTTPServer

port = 7777

handler = SimpleHTTPRequestHandler
serv = HTTPServer(('192.168.0.2', port), handler)
print('웹서비스 시작...')
serv.serve_forever()