import numpy as np


def make_board(n):
    board = np.zeros((n, n), dtype='int8')
    for i in range(n):
        for j in range(0 + i % 2, n - 1 + i % 2, 2):
            board[i][j] = 1

    return board


# print(make_board(4))
# print(make_board(6))