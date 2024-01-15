n = int(input())
m = int(input())


graph = [[1e9] * n for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -=1
    graph[a][b] = min(graph[a][b], c)


for i in range(n):
    graph[i][i] = 0


for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


for i in range(n):
    for j in range(n):
        if graph[i][j] == 1e9:
            graph[i][j] = 0

for g in graph:
    print(*g)