# coding:UTF-8
# RuHe  2025/4/15 20:36
# 螺旋矩阵
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        DIRS = (0, 1), (1, 0), (0, -1), (-1, 0)
        m, n = len(matrix), len(matrix[0])
        ans = []
        i = j = di = 0
        for _ in range(m * n):
            ans.append(matrix[i][j])
            matrix[i][j] = None
            x, y = i + DIRS[di][0], j + DIRS[di][1]
            if x < 0 or x >= m or y < 0 or y >= n or matrix[x][y] is None:
                di = (di + 1) % 4
            i += DIRS[di][0]
            j += DIRS[di][1]
        return ans


if __name__ == '__main__':
    solution = Solution()
    lst = solution.spiralOrder([[1,2,3],[4,5,6],[7,8,9]])
    print(lst)
