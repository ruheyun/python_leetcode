# 列表可变
lst = ['hello', 'a', 12]
print(lst)
lst2 = list('hello')
print(lst2)
lst3 = list(range(1, 10, 2))
print(lst3)
del lst3

# 列表遍历
print('-'*20)
for item in lst:
    print(item)

for i in range(len(lst)):
    print(i, '->', lst[i])

for index, item in enumerate(lst):
    print(index, '->', item)

# 列表的相关操作
print('-'*20)
print(lst, id(lst))
lst.append(13)
print(lst, id(lst))
lst.insert(0, 'zyc')
print(lst, id(lst))
lst.remove('a')
print(lst)
lst.pop()
print(lst)
lst.pop(1)
print(lst)
lst.reverse()
print(lst)
lst.clear()
print(lst)