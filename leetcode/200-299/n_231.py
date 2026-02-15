"""
Docstring for leetcode.n_231 2 的幂
"""


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while (not n & 1) and n > 2:
            n >>= 1
        return True if n == 1 or n == 2 else False
    
    def isPowerOfTwo_(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0