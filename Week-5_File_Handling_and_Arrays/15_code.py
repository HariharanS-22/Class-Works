import numpy as np
def transpose(mat):
    return np.transpose(mat)

mat = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Original Matrix : \n",mat)
print("Transpose of Matrix : \n",transpose(mat))
