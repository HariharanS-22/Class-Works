def linear_comb(v1, v2, a, b):
    vect=[]
    for i in range(len(v1)):
        vect.append(a*v1[i] + b*v2[i])
    return vect

v1 = [int(a) for a in input("Enter the vector 1 : ").split()]
v2 = [int(a) for a in input("Enter the vector 2 : ").split()]
a = 2
b = 3
print("Line combination of vectors : ",linear_comb(v1, v2, a, b))

