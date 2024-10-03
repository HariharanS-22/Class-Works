matA = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matB = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

result=[[sum(matA[i][k] * matB[k][j] for k in range(len(matB))) 
        for j in range(len(matB[0]))] 
        for i in range(len(matA))]
print("Matrix multiplication : ")
for row in result:
    print(row)
    
