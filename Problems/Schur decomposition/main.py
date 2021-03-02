import scipy
from scipy import linalg


A = scipy.array([[0, 2, 2], [2, 1, 2], [1, 0, 1]])

# your code here
T, Z = linalg.schur(A)
print(scipy.trace(T) + scipy.trace(Z))
