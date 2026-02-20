"""
1423. 可获得的最大点数
"""
from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        m_s = float('inf')
        s = 0
        n = len(cardPoints)
        if n == k: return sum(cardPoints)
        for i in range(n):
            s += cardPoints[i]
            if i - (n - k) + 1 >= 0:
                m_s = min(m_s, s)
                s -= cardPoints[i - (n - k) + 1]
        return sum(cardPoints) - m_s
    

# 逆向思维