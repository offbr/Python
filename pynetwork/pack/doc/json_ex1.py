'''
Created on 2016. 11. 2.

JSON
'''
import json

data = {
    'a':0,
    'b':9.6,
    'c':'Hello world',
    'd':{
        'sbs':5
    }
}
print(data) #dict type
print(type(data))
print()
json_data = json.dumps(data) #반환값이 str type / 키값들이 ""로 바뀜
print(json_data)
print(type(json_data))

print()
json_data2 = json.loads(json_data) #dict type
print(json_data2)
print(type(json_data2))

print('\n-------')
print(json.dumps(['foo',{'bar':('day', None, 1.5, 2)}]))
print(json.dumps("\"foo\bar"))

print('\n-------')
print(json.loads('["foo",{"bar":["day", null, 1.5, 2]}]'))


print('\n*************')

import codecs
def load_jsonfile(fname):
    f = codecs.open(fname, 'rb', encoding='utf-8')
    lines = f.read()
    f.close()
    jdata = json.loads(lines)
    return jdata

mydata = load_jsonfile('ftest.json')
print(mydata)
print(type(mydata))



























