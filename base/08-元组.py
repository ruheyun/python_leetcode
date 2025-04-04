# 元组不能增删改，只能创建，遍历，查找
# 1. 创建
t = ('hello', 11, ['a', 'b'])
print(t)
# 1.1 使用内置函数
t1 = tuple('hello')
print(t1)
# 2. 列表中的用法元组也适用
print('h是否在元组中：', 'h' in t1)
print('a是否不在元组中：', 'a' not in t1)
print('最大值：', max(t1))
print('最小值：', min(t1))
print('元组长度：', len(t1))
print('索引查找：', t1.index('o'))
print('统计元素个数：', t1.count('l'))
# 3. 注意只有一个元素需要加逗号
t4 = (12,)
print(t4, type(t4))
# 4. 遍历
for item in t:
    print(item, end=' ')
print()
for i in range(len(t)):
    print(i, '-->', t[i])

for index, item in enumerate(t):
    print(index, '--->', item)

# 使用方法遍历元组对象
t4 = (i for i in range(5))
print(t4.__next__())
print(t4.__next__())
print(t4.__next__())