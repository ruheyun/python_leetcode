# coding:UTF-8
# @Author:RuHe
# @Time:2024/10/4 16:39

def bubble_sort(nums: [int]) -> [int]:
    for i in range(len(nums) - 1):
        flag = False
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                flag = True
        if not flag:
            break
    return nums


def sort_array(nums: [int]) -> [int]:
    return bubble_sort(nums)


lst = [2, 4, 9, 1, 3, 5, 7]
print(sort_array(lst))
