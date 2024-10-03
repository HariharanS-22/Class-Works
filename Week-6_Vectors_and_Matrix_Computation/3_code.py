import numpy as np

def dot_prod(vect1, vect2):
    return np.dot(vect1, vect2)

list1 = [int(x) for x in input("Enter the vector 1: ").split()]
list2 = [int(x) for x in input("Enter the vector 2: ").split()]
vect1 = np.array(list1)
vect2 = np.array(list2)
print("Dot product of two vectors : ", dot_prod(vect1,vect2))
