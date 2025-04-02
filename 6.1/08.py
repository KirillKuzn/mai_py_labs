import numpy as np


def snake(m, n, direction='H'):
    arr = np.zeros((n, m), dtype='int32')
    if direction == 'H':
        for i in range(n):
            for j in range(m):
                if i % 2 == 0:
                    arr[i][j] = m * i + j + 1
                else:
                    arr[i][m - j - 1] = m * i + j + 1
    else:
        for i in range(m):
            for j in range(n):
                if i % 2 == 0:
                    arr[j][i] = n * i + j + 1
                else:
                    arr[n - j - 1][i] = n * i + j + 1
            
    return arr


# print(snake(5, 3))
# print(snake(5, 3, direction='V'))