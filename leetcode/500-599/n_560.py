# coding:UTF-8
# RuHe  2025/4/12 13:30
# 和为k的子数组
from collections import defaultdict
from typing import List


class Solution:
    """
    给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数 。
    子数组是数组中元素的连续非空序列。
    """
    def subarraySum(self, nums: List[int], k: int) -> int:
        s = [0] * (len(nums) + 1)
        for i, x in enumerate(nums):
            s[i + 1] = s[i] + x

        ans = 0
        cnt = defaultdict(int)
        for sj in s:
            ans += cnt[sj - k]
            cnt[sj] += 1
        return ans


if __name__ == '__main__':
    solution = Solution()
    cnt = solution.subarraySum([1, 1, 1], 2)
    print(cnt)
