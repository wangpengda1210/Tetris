import numpy as np

size = int(input())
fill = int(input())

if fill == 1:
    print(np.ones((size, size)))
else:
    print(np.zeros((size, size)))
