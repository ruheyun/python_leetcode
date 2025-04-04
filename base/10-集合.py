# 集合的创建，只能存储不可变数据类型， 而且无序不重复
s = {12, 13, 25}
print(s)
s1 = set([12, 45, 70])
print(s1)
# 创建空集合，只能使用set方法
s2 = {}
print(s2, type(s2))
s3 = set()
print(s3, type(s3))

s4 = set('helloworld')
print(s4)
print('-'*20)
# 集合和数学中的集合一样，有很多关于集合的操作方法
A = {10, 20, 30, 40, 50}
B = {20, 25, 50, 66}
print(A & B)
print(A | B)
print(A ^ B)
print(A - B)
print('-'*20)

# 集合的增删改
print(s)
s.add(15)
print(s)
s.remove(25)
print(s)

for item in s:
    print(item, end=' ')