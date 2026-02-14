"""
Docstring for leetcode.n_2413 最小偶倍数
"""

class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return n * 2 if n & 1 else n
    
# 找规律