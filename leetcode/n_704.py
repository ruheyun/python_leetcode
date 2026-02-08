# coding:UTF-8
# @Author:RuHe
# @Time:2024/10/19 15:08
from re import search
from typing import List


def search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1


if __name__ == '__main__':
    result = search([1, 3, 5, 7, 10, 21, 23], 10)
    print(result)
