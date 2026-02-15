"""
Docstring for leetcode.n_1740 重新排列数组
"""
from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return [num for i in range(n) for num in (nums[i], nums[i + n])]
    

# 1.循环遍历 O(n), O(n)
# 2.切片 O(n), O(1)