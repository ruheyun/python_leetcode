# coding:UTF-8
# @Author:RuHe
# @Time:2024/10/27 15:52


def guess_number(n):
    i, j = 0, n
    while i <= j:
        mid = (i + j) // 2
        if guess(mid) == 0:
            return mid
        elif guess(mid) == -1:
            j = mid - 1
        elif guess(mid) == 1:
            i = mid + 1



def guess(num):
    pass