"""
1536. 排布二进制网格的最少交换次数
"""
from typing import List


class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        lst = [n] * n
        for i in range(n):
            for j in range(n - 1, -1, -1):
                if grid[i][j]:
                    lst[i] = n - 1 - j
                    break
        
        ans = 0
        for i in range(n - 1):
            flag = n - 1 - i
            for j in range(i, n):
                if lst[j] >= flag:
                    ans += j - i
                    lst[i + 1: j + 1] = lst[i: j]
                    break
            else:
                return -1
        return ans

