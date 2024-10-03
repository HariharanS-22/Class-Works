def determinant_3x3(matrix):
    a11, a12, a13 = matrix[0]
    a21, a22, a23 = matrix[1]
    a31, a32, a33 = matrix[2]
    det = (a11 * (a22 * a33 - a23 * a32) -
           a12 * (a21 * a33 - a23 * a31) +
           a13 * (a21 * a32 - a22 * a31))
    return det
mat=[]
print("Enter the 3x3 matrix :")
for i in range(3):
    row = list(map(int,input().split()))
    mat.append(row)
print("The determinant of the matrix is:",determinant_3x3(mat))
