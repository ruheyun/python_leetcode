lst1 = [12, 19, 4, 1, 45, 8]
lst2 = ['sdd', 'hgk', 'Eef', 'aaa']

# 第一种排序，直接改变原序列
lst1.sort()
lst2.sort()
print('默认从小到大排序列表：', lst1)
print('字母按ascii码表从小到大：', lst2)
lst1.sort(reverse=True)
print('改变默认排序规则，从大到小排序：', lst1)
lst2.sort(key=str.lower)
print('改变规则，忽略大小写：', lst2)

# 第二种排序，不改变原序列，创建新的列表
new_lst1 = sorted(lst1)
print('原列表：', lst1)
print('新列表：', new_lst1)
new_lst2 = sorted(lst2, key=str.lower, reverse=True)
print('原列表：', lst2)
print('新列表：', new_lst2)

# 推导式生成列表
lst3 = [item for item in range(20) if item % 2 == 0]
print(lst3)