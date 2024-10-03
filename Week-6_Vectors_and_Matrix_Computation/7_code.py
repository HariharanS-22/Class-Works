print("Enter the elements for 2x3 matrix (row-wise):")
matA = []
for i in range(2):
    row = list(map(int,input().split()))
    matA.append(row)
matA_transpose = [[0 for j in range(2)]for i in range(3)]
for i in range(2):
    for j in range(3):
        matA_transpose[j][i] = matA[i][j]
print("Transpose of Matrix A :")
for row in matA_transpose:
    print(row)
    
        
