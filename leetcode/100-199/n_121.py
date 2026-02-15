"""
121. 买卖股票的最佳时机

给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。

你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。
设计一个算法来计算你所能获取的最大利润。

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l = len(prices)
        for i in range(l - 1):
            for j in range(i + 1, l):
                if prices[j] - prices[i] > profit:
                    profit = prices[j] - prices[i]
        return profit
    
    def maxProfit_(self, prices: List[int]) -> int:
        cost = float('+inf')
        profit = 0
        for price in prices:
            cost = min(cost, price)
            profit = max(profit, price - cost)
        return profit

