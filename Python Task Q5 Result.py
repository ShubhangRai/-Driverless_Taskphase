from matrix_operation import operations

A=[[5,8,3],
    [4,5,6],
    [7,8,9]]
  
B = [[5,8,3],
    [4,5,6],
    [7,8,9]]
result=operations()
a = (result.calc_inv(B))

def multiplication(X,Y):
    if len(X) == 3:
      result1 = [[0,0,0],[0,0,0],[0,0,0]]
    if len(X) == 2:
      result1 = [[0,0,0],[0,0,0]]
    for x in range(len(X)):
        for y in range(len(Y[0])):
            for z in range(len(Y)):
                result1[x][y] += X[x][z] * Y[z][y]
    return result1

print(multiplication(A,a))

b = (result.calc_inv(A))
print(multiplication(b,a))
