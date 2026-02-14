"""
Docstring for leetcode.n_1468 数组异或操作
"""
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        ans = 0
        for i in range(n):
            ans ^= start + 2 * i
        return ans
    
# 1.遍历 2.找规律