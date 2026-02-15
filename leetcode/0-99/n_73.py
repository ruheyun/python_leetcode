# @Version : python3
# @Author  : RuHe
# @File    : 73.py
# @Time    : 2024/9/22 15:05
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
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
    def second(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
        row_flag = False
        col_flag = False
        for i in range(rows):
            if matrix[i][0] == 0:
                row_flag = True
                break
        for i in range(cols):
            if matrix[0][i] == 0:
                col_flag = True
                break
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if row_flag:
            for i in range(rows):
                matrix[i][0] = 0
        if col_flag:
            for i in range(cols):
                matrix[0][i] = 0

if __name__ == '__main__':
    solution = Solution()
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    solution.second(matrix)
    print(matrix)