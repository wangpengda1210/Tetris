import numpy as np

matrix = np.array([[int(input()), int(input())],
                   [int(input()), int(input())]])
vector = np.array([int(input()), int(input())])

print(np.divide(matrix, vector).T)
