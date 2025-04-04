# coding:UTF-8
# @Author:RuHe
# @Time:2024/10/27 16:02


def search_insert(nums, target):
    i, j = 0, len(nums)
    while i < j:
        mid = (i + j) // 2
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            j = mid
        elif nums[mid] < target:
            i = mid + 1
    return j


if __name__ == '__main__':
    print(search_insert([1,3,5,6], 7))