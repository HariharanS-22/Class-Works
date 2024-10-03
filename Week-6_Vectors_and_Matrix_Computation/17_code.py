import numpy as np
from scipy.linalg import lu 

matrix = []
n = int(input("Enter the order of the square matrix :"))
print(f"Enter the elements of {n}x{n} matrix :")
for i in range(n):
    row = list(map(int,input().split()))
    matrix.append(row)
P, L, U = lu(matrix)
det = np.prod(np.diag(U))

print("Lower Triangular Matrix L:\n", L)
print("\nUpper Triangular Matrix U:\n", U)
print("\nDeterminant of the matrix:", det)

