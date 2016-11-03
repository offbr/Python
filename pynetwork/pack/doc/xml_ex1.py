'''
Created on 2016. 11. 1.

XML 문서 처리
'''
import xml.etree.ElementTree as etree

xmlfile = etree.parse("my.xml") 
#etree.dump(xmlfile)

print()
root = xmlfile.getroot()
print(root.tag) #items
print()
print(root[0].tag) #item
print('\n요소와 속성 읽기')
print(root[0][0].tag) #name
print(root[0][1].tag) #tel
print(root[0][0].attrib) #속성
print(root[0][2].attrib) #속성
print(root[0][2].attrib.keys())
print(root[0][2].attrib.values())

print(list(root[0][2].attrib.keys()))
print(root[0][2].attrib.get('kor'))
imsi = list(root[0][2].attrib.values())
print(imsi[0] + " " + imsi[1])

print()
myname = root.find("item").find("name").text
mytel = root.find("item").find("tel").text
print(myname + " " + mytel)

print('\n반복문-----')
for child in root:
    print(child.tag)
    for child2 in child:
        print(child2.tag, child2.attrib)

print('\n특정 요소의 속성 값 읽기')
for a in root.iter('exam'):
    print(a.attrib)

print('\n특정 요소의 속성 값 읽기')
children = root.getchildren() #root 요소의 자식 요소 얻기
print(children)
children = root.findall('item') #위와 동일
print(children)

for it in children:
    re_id = it.find('name').get('id') #속성값 읽기
    re_name = it.find('name').text #요소값
    re_tel = it.find('tel').text #요소값
    print(re_id, re_name, re_tel)





















