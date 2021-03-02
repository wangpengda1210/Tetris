import numpy
from numpy.linalg import inv
import scipy

A = numpy.array([[1, 2], [2, 3]])

# your code
print(scipy.trace(inv(A)))
