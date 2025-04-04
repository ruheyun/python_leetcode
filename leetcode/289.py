# coding:UTF-8
# @Author:RuHe
# @Time:2024/10/5 15:58
from typing import List


def gameOfLife(board: List[List[int]]) -> None:
    new_board = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 1:
                if i - 1 >= 0 and j - 1 >= 0:
                    new_board[i - 1][j - 1] += 1
                if i - 1 >=0:
                    new_board[i - 1][j] += 1
                if i - 1 >=0 and j + 1 < len(board[0]):
                    new_board[i - 1][j + 1] += 1
                if j - 1 >= 0:
                    new_board[i][j - 1] += 1
                if j + 1 < len(board[0]):
                    new_board[i][j + 1] += 1
                if i + 1 < len(board) and j -1 >= 0:
                    new_board[i + 1][j - 1] += 1
                if i + 1 < len(board):
                    new_board[i + 1][j] += 1
                if i + 1 < len(board) and j + 1 < len(board[0]):
                    new_board[i + 1][j + 1] += 1
    for i in range(len(board)):
        for j in range(len(board[0])):
            if new_board[i][j] < 2 or new_board[i][j] > 3:
                new_board[i][j] = 0
            elif new_board[i][j] == 2:
                new_board[i][j] = board[i][j]
            elif new_board[i][j] == 3:
                new_board[i][j] = 1
    print(new_board)


gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]])

