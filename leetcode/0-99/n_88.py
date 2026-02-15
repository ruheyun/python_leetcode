"""
Docstring for leetcode.n_88 合并两个有序数组
"""
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        temps = nums1[:m]
        x, i, j = 0, 0, 0
        for _ in range(m + n):
            if j == n or (i < m and temps[i] <= nums2[j]):
                nums1[x] = temps[i]
                i += 1
            else:
                nums1[x] = nums2[j]
                j += 1
            
            x += 1

    def merge_(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        x, y = m - 1, n - 1
        for i in range(m + n - 1, -1, -1):
            if y == -1:
                break
            if nums1[x] > nums2[y] and x >= 0:
                nums1[i] = nums1[x]
                x -= 1
            else:
                nums1[i] = nums2[y]
                y -= 1
            


                    
