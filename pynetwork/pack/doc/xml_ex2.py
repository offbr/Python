'''
Created on 2016. 11. 1.
기상청 제공 날씨 정보 읽기 XML
'''
import urllib.request
import xml.etree.ElementTree as etree

try:
    webdata = urllib.request.urlopen('http://www.kma.go.kr/XML/weather/sfc_web_map.xml')
    webxml = webdata.read()
    webxml = webxml.strip().decode('utf-8')
    print(webxml)
    webdata.close()
    
    with open('ftest.xml', mode='w', encoding='utf-8') as f:
        f.write(webxml)
        
    print('\nXML 파일 자료\n')
    xmlfile = etree.parse("ftest.xml")     
    root = xmlfile.getroot()
    print(root.tag)
    
    children = root.getchildren()
    for it in children:
        y = it.get('year')
        m = it.get('month')
        d = it.get('day')
        h = it.get('hour')
        print(y, '년', m, '월', d, '일', h, '시',)
        
    for child in root:
        #print(child.tag)
        for it in child:
            local_name = it.text 
            #print(local_name)
            re_ta = it.get('ta')
            
            print(local_name, '온도:', re_ta)
        
        
except Exception as e:
    print('err: ' , e)















































