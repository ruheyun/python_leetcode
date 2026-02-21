"""
3679. 使库存平衡的最少丢弃次数
"""
from typing import List
from collections import defaultdict


class Solution:
    def minArrivalsToDiscard(self, arrivals: List[int], w: int, m: int) -> int:
        cnt = defaultdict(int)
        ans = 0
        for i, x in enumerate(arrivals):
            if cnt[x] == m:
                arrivals[i] = 0
                ans += 1
            else:
                cnt[x] += 1
            if i - w + 1 >= 0:
                cnt[arrivals[i - w + 1]] -= 1
        return ans
