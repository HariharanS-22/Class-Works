import numpy as np
def add_matrices(m1, m2):
    add_mat = [[m1[i][j] + m2[i][j] for j in range(len(m1[0]))] for i in range(len(m1))]
    return np.array(add_mat)
m1 = [[1, 2, 3], [3, 4, 5]]
m2 = [[5, 6, 7], [7, 8, 9]]
print(add_matrices(m1, m2))

