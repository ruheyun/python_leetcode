# coding:UTF-8
# RuHe  2025/4/4 16:10
# 两数之和
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


if __name__ == '__main__':
    solution = Solution()
    list = solution.twoSum([2, 4, 1, 7, 0], 5)
    print(list)
