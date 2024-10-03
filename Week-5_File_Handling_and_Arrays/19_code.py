import numpy as np

def replace(arr):
    arr[arr%2==0] = 0
    return arr

arr = np.random.randint(1,100,size=10)
print("Original Array : ",arr)
print("Modified Array : ",replace(arr))
