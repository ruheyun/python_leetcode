# coding:UTF-8

import hashlib


def gcd(a, b):
    """求最大公约数"""
    while b:
        a, b = b, a % b
    return a


def get_keys(q, p):
    """计算两个密钥"""
    n = p * q
    fn = (p - 1) * (q - 1)
    e = 2
    while e < fn and gcd(fn, e) != 1:
        e += 1
    d = 2
    while e * d % fn != 1:
        d += 1
    return [n, e], [d, n]


def signature(M, sk):
    """签名过程"""
    s = M ** sk[0] % sk[1]
    return s


def verify(m, s, pk):
    """验证过程"""
    M = int(hashlib.md5(m.encode()).hexdigest(), 16) % pk[0]
    M1 = s ** pk[1] % pk[0]
    return M == M1


if __name__ == '__main__':
    # 准备公钥私钥，消息
    pk, sk = get_keys(17, 19)
    m = 'hello, Wrld!'
    M = int(hashlib.md5(m.encode()).hexdigest(), 16)
    # 签名
    s = signature(M, sk)
    # 验证
    result = verify(m, s, pk)
    print(f'公钥为{pk}，私钥为{sk}，消息为{m}，签名后为{s}，验证结果为{result}')