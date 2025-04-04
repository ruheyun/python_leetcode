# @Version : python3
# @Author  : RuHe
# @File    : 73.py
# @Time    : 2024/9/22 15:05
from typing import List


def setZeroes(matrix: List[List[int]]) -> None:
    rows = len(matrix)
    cols = len(matrix[0])
    lst_row = [False] * rows
    lst_col = [False] * cols
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                lst_row[i] = lst_col[j] = True

    for i in range(rows):
        for j in range(cols):
            if lst_row[i] or lst_col[j]:
                matrix[i][j] = 0

    print(matrix)


setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])