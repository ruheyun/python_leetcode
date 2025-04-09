# coding:UTF-8
# RuHe  2025/4/9 20:26
# 三数之和
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for k in range(len(nums) - 2):
            if nums[k] > 0 or (k > 0 and nums[k] == nums[k - 1]):
                continue
            i, j = k + 1, len(nums) - 1
            while i < j:
                s = nums[k] + nums[i] + nums[j]
                if 0 == s:
                    res.append([nums[k], nums[i], nums[j]])
                    i += 1
                    while i < j and nums[i] == nums[i - 1]: i += 1
                    j -= 1
                    while i < j and nums[j] == nums[j + 1]: j -= 1
                elif 0 > s:
                    i += 1
                    while i < j and nums[i] == nums[i - 1]: i += 1
                elif 0 < s:
                    j -= 1
                    while i < j and nums[j] == nums[j + 1]: j -= 1

        return res

if __name__ == '__main__':
    solution = Solution()
    rst = solution.threeSum([-1, 0, 1, 2, -1, -4])
    print(rst)