"""
3652. 按策略买卖股票的最佳时机
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        mpro = pro = sum(p * s for p, s in zip(prices, strategy))
        for i in range(len(strategy)):
            if strategy[i] == -1:
                pro += prices[i] * 2
            elif strategy[i] == 0:
                pro += prices[i]
            
            if i - k // 2 >= 0:
                pro -= prices[i - k // 2]
                
            if i - k + 1 >= 0:
                mpro = max(mpro, pro)
                if strategy[i - k + 1] == -1:
                    pro -= prices[i - k + 1]
                elif strategy[i - k + 1] == 1:
                    pro += prices[i - k + 1]
        return mpro


sol = Solution()
result = sol.maxProfit([4,2,8], [-1,0,1], 2)
print(result)

# 定长双窗口