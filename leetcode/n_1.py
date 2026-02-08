# coding:UTF-8
# RuHe  2025/4/4 16:10
# 两数之和
from typing import List


class Solution:
    """
    时间复杂度：n^2
    空间复杂度：1
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

class Solution2:
    """
    时间复杂度：n
    空间复杂度: n
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx = {}
        for j, x in enumerate(nums):
            if target - x in idx:
                return [idx[target - x], j]
            idx[x] = j


if __name__ == '__main__':
    solution = Solution2()
    list = solution.twoSum([2, 4, 1, 7, 0], 5)

    print(list)
