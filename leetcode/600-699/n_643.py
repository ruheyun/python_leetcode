"""
Docstring for leetcode.600-699.n_643 子数组最大平均数 I
"""
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = float('-inf')
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            if i - k + 1 >= 0:
                max_sum = max(max_sum, sum)
                sum -= nums[i - k + 1]
        return max_sum / k
    

sol = Solution()
result = sol.findMaxAverage([1,12,-5,-6,50,3], 4)
print(result)
            