"""
219. 存在重复元素 II
"""
from typing import List
from collections import defaultdict


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        cnt = defaultdict(int)
        for i, num in enumerate(nums):
            if cnt[num]:
                return True 
            cnt[num] += 1

            if i - (k + 1) + 1 >= 0:
                cnt[nums[i - k]] -= 1
        return False


print(Solution().containsNearbyDuplicate([1,2,3,1], 3))