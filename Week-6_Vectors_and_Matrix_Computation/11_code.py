def cross_product(v1, v2):
    cross_prod = [
        v1[1] * v2[2] - v1[2] * v2[1],  # i component
        v1[2] * v2[0] - v1[0] * v2[2],  # j component
        v1[0] * v2[1] - v1[1] * v2[0]   # k component
    ]
    return cross_prod
v1 = list(map(int,input("Enter the vector 1 :").split()))
v2 = list(map(int,input("Enter the vector 2 :").split()))

print("v1 x v2 = ",cross_product(v1, v2))
