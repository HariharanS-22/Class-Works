import numpy as np
mat = []
n = int(input("Enter the order of square matrix :"))
print(f"Enter the elements of {n}x{n} matrix :")
for i in range(n):
    row = list(map(int,input().split()))
    mat.append(row)
mat = np.array(mat)
eigenvalues, _ = np.linalg.eig(mat)
det = np.linalg.det(mat)
eigenvalues_prod= np.prod(eigenvalues)

print("Eigenvalues of the matrix:", eigenvalues)
print("Determinant of the matrix:", det)
print("Product of the eigenvalues:", eigenvalues_prod)
if np.isclose(det,eigenvalues_prod):
    print("Determinant and Product of Eigen values are equal")
else:
    print("Determinant and Product of Eigen values are not equal")
