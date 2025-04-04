# coding:UTF-8
# @Author:RuHe
# @Time:2024/10/5 17:07


def insertion_sort(nums: [int]) -> [int]:
    for i in range(1, len(nums)):
        j = i
        temp = nums[j]
        while j > 0 and temp < nums[j - 1]:
            nums[j] = nums[j - 1]
            j -= 1
        nums[j] = temp
    return nums


print(insertion_sort([2, 4, 9, 1, 3, 5, 7]))