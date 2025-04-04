# 字典的创建,可以使用元组作为键，不能使用列表
d1 = {10: 'dog', 12: 'cat', 15: 'zoo'}
print(d1, type(d1))
d2 = zip([10, 12, 13], ['hello', 'world', 'python'])
print(d2)
d3 = dict(d2)
print(d3)
d4 = dict(cat=10, dog=20)
print(d4)

# 字典元素的遍历
# 字典的取值，第一种如果键不存在会报错，第二种不会报错，会返回none
print(d1[10])
print(d1.get(10))

# 字典的遍历以元组的形式
for item in d1.items():
    print(item)

for key, value in d1.items():
    print(key, '-->', value)

# 获取所有键
keys = d1.keys()
print(keys, list(keys), tuple(keys))
# 获取所有值
values = d1.values()
print(values, list(values), tuple(values))
# 添加元素
d1[20] = 'Java'
print(d1)
# 删除元素，通过键删除整个键值对
d1.pop(10)
print(d1)
# 随机删除一个键值对
d1.popitem()
print(d1)
# 清空字典
d1.clear()

# 字典的推导式
d5 = {key: 'value' for key in range(5)}
print(d5)
d6 = {key: value for key, value in zip([12, 13, 14], ['hello', 'you', 'python'])}
print(d6)