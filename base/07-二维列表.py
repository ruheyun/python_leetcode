lst = [
    ['城市', '男人', '女人'],
    ['北京', 123, 234],
    ['上海', 345, 678]
]
print(lst)

# 二维列表的遍历
for row in lst:
    for item in row:
        print(item, end='\t')
    print()

# 推导式生成二维列表
lst1 = [[j for j in range(5)] for i in range(4)]
print(lst1)