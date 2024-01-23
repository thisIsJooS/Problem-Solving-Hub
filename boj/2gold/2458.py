n, m = map(int, input().split())

graph = [[1e9] * n for _ in range(n)]
for i in range(n):
    graph[i][i] = n

for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])


res = 0
for i in range(n):
    valid = True
    for j in range(n):
        if graph[i][j] == 1e9 and graph[j][i] == 1e9:
            valid = False
            break

    if valid:
        res += 1

print(res)