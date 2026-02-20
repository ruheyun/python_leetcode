"""
2461 长度为 K 子数组中的最大和
"""
from typing import List
from collections import defaultdict


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        m_s = s = 0
        dit = defaultdict(int)
        for i in range(len(nums)):
            s += nums[i]
            dit[nums[i]] += 1
            if i - k + 1 >= 0:
                if len(dit) == k:
                    m_s = max(m_s, s)
                s -= nums[i - k + 1]
                dit[nums[i - k + 1]] -= 1
                if dit[nums[i - k + 1]] == 0:
                    del dit[nums[i - k + 1]]
        return m_s
    
    def maximumSubarraySum_(self, nums: List[int], k: int) -> int:
        if k > len(set(nums)): return 0
        lst = []
        s = 0
        for i in range(len(nums)):
            if nums[i] in lst:
                lst.clear()
            lst.append(nums[i])
            if len(lst) == k:
                s = max(s, sum(lst))
                del lst[0]
        return s
    

sol = Solution()
result = sol.maximumSubarraySum_([1,5,4,2,9,9,9], 3)
print(result)