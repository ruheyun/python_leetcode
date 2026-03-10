"""
1365. 有多少小于当前数字的数字
"""
from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        for i in range(n):
            for j in range(n):
                if nums[j] < nums[i]:
                    ans[i] += 1
        return ans
    
    def other(self, nums: List[int]):
        return [sum(x < i for x in nums) for i in nums]
