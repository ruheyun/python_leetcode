# coding:UTF-8
# @Author:RuHe
# @Time:2024/10/5 16:46


def selection_sort(nums: [int]) -> [int]:
    for i in range(len(nums)):
        min_index = i
        for j in range(i+1, len(nums)):
            if nums[min_index] > nums[j]:
                min_index = j
        if min_index != i:
            nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums


print(selection_sort([2, 4, 9, 1, 3, 5, 7]))