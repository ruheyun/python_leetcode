# coding:UTF-8
# RuHe  2025/4/8 16:20
# 盛最多水的容器
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = left = 0
        right = len(height) - 1

        while left < right:
            area = (right - left) * min(height[left], height[right])
            ans = max(ans, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return ans


if __name__ == '__main__':
    solution = Solution()
    rst = solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
    print(rst)

