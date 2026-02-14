"""
Docstring for leetcode.n_1512 好数对的数目
"""
from typing import List
from collections import defaultdict


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]: ans += 1
        return ans

    def numIdenticalPairs_(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        j = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[j]:
                n = i - j
                ans += n * (n - 1) / 2
                j = i
            elif i == len(nums) - 1:
                n = i - j + 1
                ans += n * (n - 1) / 2
                j = i   
        return ans
    
    def numIdenticalPairs_1(self, nums: List[int]) -> int:
        ans = 0
        cnt = defaultdict(int)
        for x in nums:
            ans += cnt[x]
            cnt[x] += 1
        return ans
    
# 1.暴力枚举  [O(n^2), O(1)] 
# 2.排序双指针 [O(nlogn), O(1)]
# 3.遍历哈希表 [O(n), O(n)]
 
