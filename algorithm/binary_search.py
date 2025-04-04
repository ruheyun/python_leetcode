# coding:UTF-8
# @Author:RuHe
# @Time:2024/10/16 20:11
from typing import List


def binary_search(T: List[int], x: int) -> int:
    # 二分查找
    l = 1
    r = len(T)
    while l <= r:
        m = (l + r) // 2
        if T[m] == x:
            return m
        elif T[m] < x:
            l = m + 1
        else:
            r = m - 1
    return -1


if __name__ == '__main__':
    lst = [1, 3, 5, 7, 8, 10, 21, 25]
    target = 24
    result = binary_search(lst, target)
    print(result)


