# coding:UTF-8
# RuHe  2025/4/12 21:13
# 区域和检索--数组不可变
from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        s = [0] * (len(nums) + 1)
        for i, x in enumerate(nums):
            s[i + 1] = s[i] + x
        self.s = s

    def sumRange(self, left: int, right: int) -> int:
        return self.s[right + 1] - self.s[left]

