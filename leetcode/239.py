# coding:UTF-8
# RuHe  2025/4/13 17:11
# 滑动窗口的最大值
from collections import deque
from typing import List


class Solution:
    """
    给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧,
    你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
    返回 滑动窗口中的最大值 。
    """
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        ans = []
        for i, x in enumerate(nums):
            while q and nums[q[-1]] <= x:
                q.pop()
            q.append(i)
            if i - q[0] >= k:
                q.popleft()
            if i >= k - 1:
                ans.append(nums[q[0]])
        return ans


if __name__ == '__main__':
    solution = Solution()
    rst = solution.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)
    print(rst)
