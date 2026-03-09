"""
645. 错误的集合
"""
from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans = [0, 0]
        left = 0
        for i, x in enumerate(nums):
            x = abs(x)
            if nums[x - 1] < 0:
                ans[0] = x - 1
                continue
            nums[x - 1] = - nums[x - 1]
            while nums[left] < 0:
                left += 1
        ans[1] = left + 1
        return ans
