# coding:UTF-8
# @Author:RuHe
# @Time:2024/10/5 17:34


def shell_sort(nums: [int]) -> [int]:
    gap = len(nums) // 2
    while gap > 0:
        for i in range(gap, len(nums)):
            j = i
            temp = nums[j]
            while j > 0 and temp < nums[j - gap]:
                nums[j] = nums[j - gap]
                j -= gap
            nums[j] = temp
        gap //= 2
    return nums


print(shell_sort([2, 4, 9, 1, 3, 5, 7]))