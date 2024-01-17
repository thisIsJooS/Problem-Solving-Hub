A = input()
B = input()
a, b = len(A), len(B)

mat = [[0]*(a+1) for _ in range(b+1)]


for i in range(1, b+1):
    for j in range(1, a+1):

        if B[i-1] == A[j-1]:
            mat[i][j] = 1 + mat[i-1][j-1]

        else:
            mat[i][j] = max(mat[i-1][j], mat[i][j-1])

print(mat[b][a])
