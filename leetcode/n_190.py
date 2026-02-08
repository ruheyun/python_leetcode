"""
Docstring for leetcode.n_190
颠倒给定的 32 位有符号整数的二进制位。
"""
class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(31):
            ans += n & 1
            ans <<= 1
            n >>= 1
        return ans
