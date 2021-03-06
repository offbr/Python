'''
set : {}를 사용. 순서X. 중복X (중복된 데이터 제거할 때 효과적)
'''
a = {1, 2, 3}
print(a, len(a))
b = {3, 4}
print(a.union(b))
print(a.intersection(b))
print(a | b, a - b, a & b)

#print(b[0]) #TypeError: 'set' object does not support indexing
b.add(5)
print(b)
b.update({5, 6})
print(b)
b.update([7, 8])
print(b)
b.update((9, 10))
print(b)

print()
b.discard(7) #값에 의한 삭제
b.remove(8) #값에 의한 삭제
b.discard(7) #값이 없어도 에러X
#b.remove(8) #값이 없으면 에러O
print(b)

b.clear()
print(b)

#중복 자료 제거
li = [1,2,2,1,3]
print(li)
s = set(li)
li = list(s)
print(s)
































