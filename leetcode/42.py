# coding:UTF-8
# RuHe  2025/4/10 21:45
# 接雨水
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left, right, pre_max, suf_max, ans = 0, len(height) - 1, 0, 0, 0
        while left < right:
            pre_max = max(pre_max, height[left])
            suf_max = max(suf_max, height[right])
            if pre_max < suf_max:
                ans += pre_max - height[left]
                left += 1
            else:
                ans += suf_max - height[right]
                right -= 1
        return ans


if __name__ == '__main__':
    solution = Solution()
    rst = solution.trap([0,1,0,2,1,0,1,3,2,1,2,1])
    print(rst)

