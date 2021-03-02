import numpy as np

a = int(input())
b = int(input())
c = int(input())
d = int(input())

matrix = np.array([[a, b], [c, d]])
print(np.linalg.svd(matrix))
