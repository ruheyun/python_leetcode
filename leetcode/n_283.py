# coding:UTF-8
# RuHe  2025/4/6 23:32
# 移动零
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i, num in enumerate(nums):
            if num != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1


if __name__ == '__main__':
    solution = Solution()
    nums_list = [0,1,0,3,12]
    solution.moveZeroes(nums_list)
    print(nums_list)
