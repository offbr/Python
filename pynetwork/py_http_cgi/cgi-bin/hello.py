#!/usr/local/bin/python3.5
import cgi
ss = '이건 파이썬 변수 값이야~'
print('Content-Type:text/html;charset=utf-8\n')
print('<html><body>')
print('<b>안녕 난 파이썬이라고 해</b><br/>')
print('변수 값 : %s'%(ss,))
print('</body></html>')

