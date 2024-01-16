"""
5 4
0 1 0 1 1
1 0 1 1 0
0 1 0 0 0
1 1 0 0 0
1 0 0 0 0
2 3 4 3
"""
n, m = map(int, input().split())


mat = []
for i in range(n):
    line = list(map(int, list(input())))
    for j in range(n):
        if i != j and line[j] == 0:
            line[j] = 1e9

    mat.append(line)


for k in range(n):
    for i in range(n):
        for j in range(n):
            mat[i][j] = min(mat[i][j], mat[i][k] + mat[k][j])


path = list(map(int, input().split()))
for i in range(m-1):
    if mat[path[i]][path[i+1]] == 1e9 and mat[path[i+1]][path[i]] == 1e9:
        print('NO')
        exit(0)

print('YES')



