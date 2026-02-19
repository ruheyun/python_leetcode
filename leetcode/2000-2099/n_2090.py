"""
Docstring for leetcode.2000-2099.n_2090 半径为 k 的子数组平均值
"""
from typing import List


class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        sum = 0
        avgs = [-1] * n

        if k == 0:
            return nums
        
        if 2 * k + 1 > n:
            return avgs
        
        for i in range(n):
            sum += nums[i]
            if i - 2 * k >= 0:
                avgs[i - k] = sum // (2 * k + 1)
                sum -= nums[i - 2 * k]
        return avgs

sol = Solution()
result = sol.getAverages([7,4,3,9,1,8,5,2,6], 3)
print(result)