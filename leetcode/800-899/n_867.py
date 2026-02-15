"""
Docstring for leetcode.n_867 转置矩阵
"""
from typing import List


def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
    m, n = len(matrix), len(matrix[0])
    ans = [[0] * m for _ in range(n)] 
    for i, row in enumerate(matrix):
        for j, x in enumerate(row):
            ans[j][i] = x
    return ans