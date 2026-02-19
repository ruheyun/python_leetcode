"""
Docstring for leetcode.1300-1399.n_1343 大小为 K 且平均值大于等于阈值的子数组数目
"""
from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        sum = 0
        count = 0
        for i in range(len(arr)):
            sum += arr[i]
            if i - k + 1 >= 0:
                if sum >= k * threshold:
                    count += 1
                sum -= arr[i - k + 1]
        return count
