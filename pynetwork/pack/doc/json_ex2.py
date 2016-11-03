'''
Created on 2016. 11. 2.

json 처리
'''
import codecs
import json

json_file = "./ftest.json"
jsondata = {}

def readData(filename):
    f = codecs.open(filename, 'rb', encoding='utf-8')
    lines = f.read()
    f.close
    jdata = json.loads(lines)
    return jdata

def main():
    global json_file
    global jsondata
    jsondata = readData(json_file)
    print(jsondata)
    d1 = jsondata['직원']['이름']
    d2 = jsondata['직원']['직급']
    d3 = jsondata['직원']['번호']
    print(d1, '/', d2, '/', d3)
    
    d4 = jsondata['웹사이트']['카페명']
    d5 = jsondata['웹사이트']['userid']
    print(d4, '/', d5)
    
if __name__ == '__main__':
    main()























