#!/usr/local/bin/python3.5
'''
Created on 2016. 11. 3.

결과는 브라우저로 전송
'''
ss1 = '이건 파이썬 변수 값이야~'
ss2 = '두 번째 자료'
print('Content-Type:text/html;charset=utf-8\n')
print(
'''
<html><body>
<h2>** 월드 화면 **</h2>
자료 : {0}, {1}
<br>
<img src ='../images/logo.png' width='60%'/>
<br>
<a href='../main.html'>메인으로</a>
</body></html>
'''.format(ss1,ss2)    
)

