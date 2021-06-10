#Python Task Q1.c Shubhang.py
A = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
B = [[10, 11, 12],[13, 14, 15],[16, 17, 18]]

result = [[sum(a * b for a, b in zip(A_row, B_col))
                        for B_col in zip(*B)]
                                for A_row in A]

r = [[84, 90, 96],[201, 216, 231],[318, 342, 366]];

rez = [[r[j][i] for j in range(len(r))] for i in range(len(r[0]))]
print("\n")
print("(AB)^T=")
for row in rez:
    print(row)

rez = [[B[j][i] for j in range(len(B))] for i in range(len(B[0]))]
print("\n")

rez = [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]

X = [[10, 13, 16],[11, 14, 17],[12, 15, 18]]

Y = [[1, 4, 7],[2, 5, 8],[3, 6, 9]]
print("\n")

print("B^T*B^T=")

result = [[sum(x * y for x, y in zip(X_row, Y_col))
                        for Y_col in zip(*Y)]
                                for X_row in X]
for r in result:
    print(r)
print("\n")
print("Hence proven,as equal")
