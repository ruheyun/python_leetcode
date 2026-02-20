"""
2841 几乎唯一子数组的最大和
"""
from typing import List
from collections import defaultdict


class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        if m > k or m > len(set(nums)):
            return 0
        s = 0
        max_s = 0
        dit = defaultdict(int)
        for i in range(len(nums)):
            s += nums[i]
            dit[nums[i]] += 1
            if i - k + 1 >= 0:
                if len(dit) >= m:
                    max_s = max(max_s, s)
                s -= nums[i - k + 1]
                dit[nums[i - k + 1]] -= 1
                if dit[nums[i - k + 1]] == 0:
                    del dit[nums[i - k + 1]]
        return max_s
