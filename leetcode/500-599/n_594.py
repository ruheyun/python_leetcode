"""
594. 最长和谐子序列
"""
from collections import Counter
from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        ans = 0
        for x, c in cnt.items():
            if x + 1 in cnt:
                ans = max(ans, c + cnt[x + 1])
        return ans



