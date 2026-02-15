"""
Docstring for leetcode.n_326 3 的幂
"""


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n % 3 == 0 and n > 3:
            n //= 3
        return True if n == 1 or n == 3 else False