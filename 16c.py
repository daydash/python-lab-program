# Program on linear algebra
 
import numpy as np
from scipy import linalg
from scipy.linalg import eigh
A = np.array([[6,3], [5,2]])
B = linalg.inv(A)
print(B)
c = linalg.det(A)
print(c)
D = np.array([[1, 3, 2, 4], [1, 5, 6, 3], [6, 3, 4, 1], [4, 3, 2, 5]])
a, b = eigh(D)

print("Selected eigenvalues:", a)
print("Complex ndarray:", b)
