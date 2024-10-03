# Main program
import matrix_operations as mat_op

m, n = map(int, input("Enter the order of the matrix (rows columns): ").split())
A=[]
B=[]
print(f"Enter the {m} x {n} matrix A : ")
for i in range(m):
    q=[]
    for j in range(n):
        a=int(input())
        q.append(a)
    A.append(q)
print(f"Enter the {m} x {n} matrix B : ")
for i in range(m):
    q=[]
    for j in range(n):
        a=int(input())
        q.append(a)
    B.append(q)
 
print("Addition of matrix A and B : \n",mat_op.add(A,B))
print("Subtraction of matrix A and B : \n",mat_op.sub(A,B))
print("Multiplication of matrix A and B :\n",mat_op.multiply(A,B))
        
        