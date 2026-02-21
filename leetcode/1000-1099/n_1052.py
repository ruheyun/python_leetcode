"""
1052. 爱生气的书店老板
"""
from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        ans = sum(c for c, g in zip(customers, grumpy) if g == 0)
        m_s = 0
        for i, x in enumerate(customers):
            if grumpy[i] == 1:
                ans += x
            if i - minutes + 1 >= 0:
                m_s = max(m_s, ans)
                if grumpy[i - minutes + 1] == 1:
                    ans -= customers[i - minutes + 1]
        return m_s 
