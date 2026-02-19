# def ext_gcd(a, b): #扩展欧几里得算法
#     if b == 0:
#         return 1, 0, a
#     else:
#         x, y, gcd = ext_gcd(b, a % b) #递归直至余数等于0(需多递归一层用来判断)
#         x, y = y, (x - (a // b) * y) #辗转相除法反向推导每层a、b的因子使得gcd(a,b)=ax+by成立
#         return x, y, gcd


# print(ext_gcd(1848, 701))


# import numpy as np
# a = np.arange(24).reshape(2, 3, 4)
# print(f'原数组：{a}，形状为：{a.shape}')
# b = np.rollaxis(a, 2, 0)
# print(f'b数组为：{b}, 形状为：{b.shape}')
# c = a.reshape(4, 2, 3)
# print(f'c数组为：{c}, 形状为：{c.shape}')

print(int(True))

