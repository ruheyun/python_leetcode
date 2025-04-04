from typing import List


def rotate(matrix: List[List[int]]) -> None:
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows - 1):
        for j in range(i + 1, cols):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(rows):
        for j in range(cols // 2):
            matrix[i][j], matrix[i][cols - 1 - j] = matrix[i][cols - 1 - j], matrix[i][j]
    print(matrix)


rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])