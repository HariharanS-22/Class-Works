import numpy as np
def check_lineardependent(v1, v2):
    return np.linalg.matrix_rank([v1, v2]) < 2

v1 = list(map(int,input("Enter the vector 1 :").split()))
v2 = list(map(int,input("Enter the vector 2 :").split()))
if check_lineardependent(v1,v2):
    print("The given vectors are linearly dependent")
else:
    print("The given vectors are linearly independent")