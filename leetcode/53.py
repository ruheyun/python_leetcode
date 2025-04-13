# coding:UTF-8
# RuHe  2025/4/13 18:22
# 最大子数组和

"""
给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
子数组是数组中的一个连续部分。
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = max(nums)
        if ans <= 0: return ans
        sum = 0
        for num in nums:
            sum = max(sum + num, 0)
            ans = max(ans, sum)
        return ans
