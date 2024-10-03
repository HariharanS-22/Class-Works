import numpy as np
from scipy.linalg import svd
matrix = []
n = int(input("Enter the order of the square matrix :"))
print(f"Enter the elements of {n}x{n} matrix :")
for i in range(n):
    row = list(map(int,input().split()))
    matrix.append(row)
    
threshold=1e-10
U, singular, VT = svd(matrix)
rank = np.sum(singular > threshold)

print("Matrix U (left singular vectors):\n", U)
print("\nSingular values:\n", singular)
print("\nMatrix V^T (right singular vectors):\n", VT)
print("\nRank of the matrix:", rank)

