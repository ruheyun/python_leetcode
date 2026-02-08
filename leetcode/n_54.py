# @Version : python3
# @Author  : RuHe
# @File    : 54.py
# @Time    : 2024/9/22 15:36
from typing import List


def spiralOrder(matrix: List[List[int]]) -> List[int]:
    l, r, t, b, lst = 0, len(matrix[0]) - 1, 0, len(matrix) - 1, []
    while True:
        for i in range(l, r + 1):
            lst.append(matrix[t][i])
        t += 1
        if t > b:
            break

        for i in range(t, b + 1):
            lst.append(matrix[i][r])
        r -= 1
        if r < l:
            break

        for i in range(r, l - 1, -1):
            lst.append(matrix[b][i])
        b -= 1
        if b < t:
            break

        for i in range(b, t - 1, -1):
            lst.append(matrix[i][l])
        l += 1
        if l > r:
            break

    return lst


print(spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))

