#Shubhang- Q1. a)
X = [[5,7,12], [13,2,7],[69,69,69]]
Y = [[7,7,7],[22,3,1],[3,2,1]]
def product_mat(mat1,mat2):
    a = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(len(mat1)):
       for j in range(len(mat2[0])):
         for k in range(len(mat2)):
            a[i][j] += mat1[i][k] * mat2[k][j]
    return a
result=product_mat(X,Y)
print(result)
