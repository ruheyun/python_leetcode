# @Version : python3
# @Author  : RuHe
# @File    : 59.py
# @Time    : 2024/9/22 16:18
from typing import List


def generateMatrix(n: int) -> List[List[int]]:
    matrix = [[0 for i in range(n)] for i in range(n)]
    l, r, t, b, count = 0, n - 1, 0, n - 1, 1
    while True:
        for i in range(l, r + 1):
            matrix[t][i] = count
            count += 1
        t += 1
        if t > b:
            break

        for i in range(t, b + 1):
            matrix[i][r] = count
            count += 1
        r -= 1
        if r < l:
            break

        for i in range(r, l - 1, -1):
            matrix[b][i] = count
            count += 1
        b -= 1
        if b < t:
            break

        for i in range(b, t - 1, -1):
            matrix[i][l] = count
            count += 1
        l += 1
        if l > r:
            break

    return matrix


print(generateMatrix(5))