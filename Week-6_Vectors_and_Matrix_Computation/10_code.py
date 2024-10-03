import numpy as np
def rank_matrix(matrix):
    return np.linalg.matrix_rank(matrix)

m,n = map(int,input("Enter the order of the matrix :").split())
mat=[]
print(f"Enter the {m}x{n} matrix :")
for i in range(m):
    row = list(map(int,input().split()))
    mat.append(row)
print("Rank of the given matrix :",rank_matrix(mat))