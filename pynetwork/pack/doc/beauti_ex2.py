'''
Created on 2016. 11. 2.

@author: All
'''
from bs4 import BeautifulSoup 
from urllib.request import urlopen 

html = urlopen("http://naver.com") 
soup = BeautifulSoup(html.read(), "lxml") 

for row in soup.find_all("ol"):
    #print(row) 
    for i in range(11):
        try: 
            li = row.find_all("li", attrs={"value":str(i)}) 
            st1 = str(li).split(">")[1]
            st2 = st1.split("title=")[1] #인터파크  따위의 인기검색어
            print("%d => %s" % (i, st2)) 
        except: 
            print("--- 네이버 인기 검색어 ---") 
