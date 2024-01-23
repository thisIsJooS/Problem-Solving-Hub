def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = int(input()), int(input())

graph = []
parent = [i for i in range(n)]
for i in range(n):
    line = list(map(int, input().split()))

    for j in range(i+1, n):
        if line[j] == 1:
            union(i, j)

    graph.append(line)



path = list(map(int, input().split()))
for i in range(m-1):
    if find_parent(path[i]-1) != find_parent(path[i+1]-1):
        print('NO')
        exit(0)

print('YES')


"""
5
4
0 1 0 1 0
1 0 1 1 0
0 1 0 0 0
1 1 0 0 0
0 0 0 0 0
2 3 4 5
"""


# n, m = int(input()), int(input())
#
#
# mat = []
# for i in range(n):
#     line = list(map(int, input().split()))
#     for j in range(n):
#         if i != j and line[j] == 0:
#             line[j] = 1e9
#
#     mat.append(line)
#
#
# for k in range(n):
#     for i in range(n):
#         for j in range(n):
#             mat[i][j] = min(mat[i][j], mat[i][k] + mat[k][j])
#

path = list(map(int, input().split()))
for i in range(m-1):
    if mat[path[i]-1][path[i+1]-1] == 1e9 and mat[path[i+1]-1][path[i]-1] == 1e9:
        print('NO')
        exit(0)

print('YES')
