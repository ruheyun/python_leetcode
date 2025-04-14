from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    """
    时间复杂度：n
    空间复杂度：n
    """
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

def productExceptSelf2(nums: List[int]) -> List[int]:
    """
    优化方法一
    时间复杂度：n
    空间复杂度：1
    """
    ans, tmp = [1] * len(nums), 1
    for i in range(1, len(nums)):
        ans[i] = ans[i - 1] * nums[i - 1]
    for i in range(len(nums) - 2, -1, -1):
        tmp *= nums[i + 1]
        ans[i] *= tmp
    return ans


if __name__ == '__main__':
    print(productExceptSelf2([1,2,3,4]))

