def determinant_2x2(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
mat = []
print("Enter a 2x2 matrix :")
for i in range(2):
    row = list(map(int,input().split()))
    mat.append(row)   
print("Determinant :",determinant_2x2(mat))