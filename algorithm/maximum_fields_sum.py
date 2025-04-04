# coding:UTF-8
# @Author:RuHe
# @Time:2024/10/16 20:26


def maximum_fields_sum(lst: [int]) -> int:
    i = 1
    j, m, n = 0, 0, 0
    sum = lst[0]
    max_sum = lst[0]
    while i < len(lst):
        sum += lst[i]
        if sum > max_sum:
            max_sum = sum
            m = j
            n = i
        elif sum <= 0:
            sum = 0
            j = i + 1
        i += 1
    return m, n


if __name__ == '__main__':
    lst = [2, -4, 4, 9, -2, 3, -10, -2]
    m, n = maximum_fields_sum(lst)
    print(m, n)