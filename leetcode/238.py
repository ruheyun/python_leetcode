from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    n = len(nums)
    lst_l, lst_r = [1] * n, [1] * n
    answer = []
    for i in range(1, n):
        lst_l[i] = lst_l[i - 1] * nums[i - 1]

    for i in range(n - 2, -1, -1):
        lst_r[i] = lst_r[i + 1] * nums[i + 1]

    for i in range(n):
        answer.append(lst_l[i] * lst_r[i])

    return answer


print(productExceptSelf([1,2,3,4]))

