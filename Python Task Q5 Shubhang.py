#Python Task Q5 Shubhang
#PS. ONLY MADE THE FUNCTIONS
def transposeMatrix(m):
    return list(map(list,zip(*m)))
def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]
def getMatrixDeternminant(m):

    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]
    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*getMatrixDeternminant(getMatrixMinor(m,0,c))
    return determinant
def getMatrixCofactors(m):

    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMatrixMinor(m,r,c)
            cofactorRow.append(((-1)**(r+c)) * getMatrixDeternminant(minor))
        cofactors.append(cofactorRow)
    cofactors = transposeMatrix(cofactors)
    return cofactors
def getMatrixInverse(m):
    determinant = getMatrixDeternminant(m)
    cofactor=getMatrixCofactors(m)

    if len(m) == 2:
        return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                [-1*m[1][0]/determinant, m[0][0]/determinant]]
    for r in range(len(cofactor)):
        for c in range(len(cofactor)):
            cofactor[r][c] = cofactor[r][c]/determinant
    return cofactor

print(getMatrixInverse([[5,8,3],
                         [4,5,6],
                         [7,8,9]]))
