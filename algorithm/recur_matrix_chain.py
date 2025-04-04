# coding:UTF-8
# @Author:RuHe
# @Time:2024/10/28 16:01
import math


def recur_matrix_chain(P, i, j):
    if i == j:
        m = 0
        return m
    m = math.inf
    for k in range(i, j):
        q = recur_matrix_chain(P ,i, k) + recur_matrix_chain(P, k + 1, j) + P[i - 1] * P[k] * P[j]
        if q < m:
            m = q
    return m


def matrix_chain(P, n):
    m = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for r in range(2, n + 1):
        for i in range(1, n - r + 1 + 1):
            j = i + r - 1
            m[i][j] = m[i + 1][j] + P[i - 1] * P[i] * P[j]
            for k in range(i + 1, j - 1 + 1):
                t = m[i][k] + m[k + 1][j] + P[i - 1] * P[k] * P[j]
                if t < m[i][j]:
                    m[i][j] = t
    print(m[1][n])


if __name__ == '__main__':
    # print(recur_matrix_chain([30, 35, 15, 5, 10, 20], 1, 5))
    matrix_chain([30, 35, 15, 5, 10, 20], 5)