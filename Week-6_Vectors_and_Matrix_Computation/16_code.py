def solve_2var_linear(a1, b1, c1, a2, b2, c2):
    D = a1 * b2 - a2 * b1
    if D == 0:
        return "The system has no unique solution (determinant is zero)."
    D_x = c1 * b2 - c2 * b1
    D_y = a1 * c2 - a2 * c1
    x = D_x / D
    y = D_y / D
    return x, y
a1, b1, c1 = map(int,input("Enter the coefficient of first equation (ax+by=c) :").split())
a2, b2, c2 = map(int,input("Enter the coefficient of second equation (ax+by=c) :").split()) 
print("The solution is:", solve_2var_linear(a1, b1, c1, a2, b2, c2))
