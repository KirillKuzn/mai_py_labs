import numpy as np


def multiplication_matrix(n):
    matrix = np.zeros((n, n), dtype='int32')
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            matrix[i - 1][j - 1] = i * j

    return matrix


# print(multiplication_matrix(3))
# print(multiplication_matrix(5))