from typing import List


def rotate(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    while k > 0:
        num = nums.pop()
        nums.insert(0, num)
        k -= 1
    print(nums)

rotate([1, 2, 3, 4, 5], 3)