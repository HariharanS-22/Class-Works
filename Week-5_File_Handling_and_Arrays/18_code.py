import numpy as np

def index_large(arr):
    return np.argmax(arr)

arr = np.random.randint(1,100,size=10)
print("Array : ",arr)
print("Index of the largest number : ",index_large(arr))
