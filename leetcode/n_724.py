from typing import List


def pivotIndex(nums: List[int]) -> int:
    sum_2 = 0
    for i in range(len(nums)):
        sum_1 = (sum(nums) - nums[i]) / 2
        if sum_2 == sum_1:
            return i
        sum_2 = sum_2 + nums[i]
    return -1

print(pivotIndex([1,7,3,6,5,6]))