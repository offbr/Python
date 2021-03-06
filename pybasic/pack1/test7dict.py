'''
dict : {'키','값'}, json형식과 유사. 순서X.
'''
mydic = dict(k1=1, k2='abc', k3=3.4)
print(mydic)

print()
coffee = {'espresso':'에스프레소', 'latte':'라떼'}
print(coffee, len(coffee))
print(coffee['espresso'])
#print(coffee['에스프레소']) #KeyError: '에스프레소' 키에 의해서 값을 찾는다.
#print(coffee[0]) #KeyError: 0 순서가 없으므로 못 찾는다.

print(coffee.keys())
print(coffee.values())
print(coffee.items())

print(list(coffee.keys())) #형변환
print(coffee.get('latte'))

print()
print('latte' in coffee)
print('cola' in coffee)

print()
coffee['cappuccino'] = '카푸치노'
print(coffee)

del coffee['cappuccino']
print(coffee)

coffee.clear()
print(coffee)


















