import numpy as np

def scalar_multiply(k,vect1):
    return k*vect1

k = int(input("Enter the scalar multiple : "))
list1=[int(a) for a in input("Enter the vector : ").split()]
vector = np.array(list1)
print("Scalar multiplication : ",scalar_multiply(k, vector))


