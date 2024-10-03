import numpy as np
vectors = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]
rank = np.linalg.matrix_rank(vectors)
if rank == len(vectors):
    print(f"The set of vectors {vectors} forms a basis")
else:
    print("The set of vectors does not form a basis")
