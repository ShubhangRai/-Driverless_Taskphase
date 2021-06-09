X = [[1,2],[3 ,4],[5 ,6]]
a = [[0,0,0],[0,0,0]]
for i in range(len(X)):
 for j in range(len(X[0])):
  a[j][i] = X[i][j]
for r in a:
   print(r)
