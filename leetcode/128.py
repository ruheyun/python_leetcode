# coding:UTF-8
# RuHe  2025/4/7 21:27
# 最长连续序列
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        st = set(nums)
        for x in st:
            if x - 1 in st:
                continue

            y = x + 1
            while y in st:
                y += 1

            ans = max(ans, y - x)
        return ans


if __name__ == '__main__':
    solution = Solution()
    out = solution.longestConsecutive([100,4,200,1,3,2])
    print(out)

