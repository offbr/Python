'''
Created on 2016. 11. 3.

동적 서버
'''
from http.server import CGIHTTPRequestHandler, HTTPServer

port = 8888

class Handler(CGIHTTPRequestHandler):
    cg_directories = ['/cgi-bin']

serv = HTTPServer(('192.168.0.2', port), Handler)

print('웹서버 서비스 중...')
serv.serve_forever()

#sudo chmod a+x sangpum.py