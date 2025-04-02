import numpy as np


def stairs(vector: np.array):
    n = vector.size
    matrix = np.zeros((n, n), dtype="int16")
    matrix[0] = vector
    for i in range(1, n):
        for j in range(n):
            matrix[i][(i + j) % n] = vector[j]

    return matrix


# print(stairs(np.arange(3)))
# print(stairs(np.arange(5)))