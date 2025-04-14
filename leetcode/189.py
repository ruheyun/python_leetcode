from typing import List


def rotate(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    k %= len(nums)
    while k > 0:
        num = nums.pop()
        nums.insert(0, num)
        k -= 1
    print(nums)


if __name__ == '__main__':
    rotate([1, 2, 3, 4, 5], 8)