# coding:UTF-8
# RuHe  2025/4/14 20:35
# 缺失的第一个正数
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        tmp = 1
        if tmp not in nums:
            return tmp
        l = len(nums)
        for i in range(l):
            cur = min(nums)
            if cur <=0:
                nums.remove(cur)
                continue
            if cur - tmp > 1:
                return tmp + 1
            tmp = cur
            nums.remove(cur)
        return tmp + 1

    def second(self, nums: List[int]) -> int:
        l = len(nums)
        for a in nums:
            while 0 < a <= l and a != nums[a - 1]:
                nums[a - 1], a = a, nums[a - 1]
        for i in range(l):
            if i + 1 != nums[i]:
                return i + 1
        return l + 1


if __name__ == '__main__':
    solution = Solution()
    rst = solution.second([3,4,-1,1])
    print(rst)
