# coding:UTF-8

import hashlib
import math
import random


def gcd(a, b):
    """求最大公约数"""
    while b:
        a, b = b, a % b
    return a


def is_prime(n):
    """判断是否为素数"""
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def euler(n):
    """欧拉函数"""
    if is_prime(n):
        return n - 1
    m = 0
    for i in range(n):
        if gcd(i, n) == 1:
            m += 1
    return m


def get_first_primitive_root(p):
    """求第一个本原元"""
    euler_n = euler(p)
    for a in range(2, p):
        for m in range(2, p):
            if pow(a, m, p) == 1:
                if m == euler_n:
                    return a
                else:
                    break
    return False


def get_all_primitive_root(p):
    """获取所有本原元"""
    all_primitive_roots = []
    first = get_first_primitive_root(p)
    euler_n = euler(p)
    for i in range(euler_n):
        if gcd(i, euler_n) == 1:
            a = pow(first, i, p)
            all_primitive_roots.append(a)
    return all_primitive_roots


def get_inverse_element(a, b):
    """获取随机数k逆元"""
    if b == 0:
        return 1, 0
    else:
        x, y = get_inverse_element(b, a % b)
        x, y = y, (x - (a // b) * y)
        return x, y


def signature(g, m, x, p):
    """签名过程"""
    # 计算m哈希值
    hm = int(hashlib.md5(m.encode()).hexdigest(), 16)
    # 选择随机k，并求逆元
    k = random.randint(2, p - 1)
    while gcd(k, p - 1) != 1:
        k = random.randint(2, p - 1)
    _, k_ = get_inverse_element(p - 1, k)
    # 计算r
    r = pow(g, k, p)
    # 计算s
    s = (hm - x * r) * k_ % (p - 1)
    return r, s, k


def verify(m, r, s, y, g, p):
    """验证过程"""
    hm = int(hashlib.md5(m.encode()).hexdigest(), 16)
    m1 = pow(y, r, p) * pow(r, s, p) % p
    m2 = pow(g, hm, p)
    # print(m1, m2)
    return m1 == m2


if __name__ == '__main__':
    # 大素数
    p = 53
    # 随机本原元
    zp = get_all_primitive_root(p)
    g = zp[random.randint(0, len(zp) - 1)]
    # 私钥，随机一个x
    x = random.randint(1, p - 2)
    # 公钥，y
    y = pow(g, x, p)
    # 待签名消息
    m = 'hello, World!'
    # 签名
    r, s, k = signature(g, m, x, p)
    # 验证
    result = verify(m, r, s, y, g, p)
    print(f'大素数p为：{p}，随机本元g为：{g}，私钥x为：{x}，公钥y为：{y}，信息m为：{m}，随机数k为：{k}，r为：{r}，s为：{s}，结果为：{result}')