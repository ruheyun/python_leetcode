"""
1689. 十-二进制数的最少数目
"""


class Solution:
    def minPartitions(self, n: str) -> int:
        m = 0
        for i in n:
            m = max(m, int(i))
        return m
    
# int(max(n))
# 十进制数字中各个位上数最大的那个