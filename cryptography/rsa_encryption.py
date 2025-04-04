# coding:UTF-8
# @Author:RuHe
# @Time:2024/10/31 10:29


# 求两个数字的最大公约数（欧几里得算法）
def gcd(a, b):
   if b == 0:
       return a
   else:
       return gcd(b, a % b)

# 获取密钥
def get_key(p, q):
   n = p * q
   fyn = (p - 1) * (q - 1)
   print(fyn)
   e = 2
   while gcd(e, fyn) != 1:
       e = e + 1
   d = 2
   while (e*d) % fyn != 1:
       d = d + 1
   print(d)
   return (n, e), (n, d)


# 加密
def encryption(x, pubkey):
   n = pubkey[0]
   e = pubkey[1]
   y = x ** e % n   # 加密
   return y


# 解密
def decryption(y, prikey):
   n = prikey[0]
   d = prikey[1]
   x = y ** d % n      # 解密
   return x


if __name__ == '__main__':
   p = int(input("请给定第一个质数p的值："))
   q = int(input("请给定第二个质数q的值："))
   x = int(input("请给定要加密的消息x的值："))
   # 生成公钥私钥
   pubkey, prikey = get_key(p, q)
   print("加密前的消息是：", x)
   y = encryption(x, pubkey)
   print("加密后的消息是：", y)
   after_x = decryption(y, prikey)
   print("解密后的消息是：", after_x)

