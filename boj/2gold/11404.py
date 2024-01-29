import sys
input = sys.stdin.readline

n, m = int(input()), int(input())
graph = [[1e9] * (n+1) for _ in range(n+1)]

for i in range(n+1):
    graph[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)


for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


for g in graph[1:]:
    g = g[1:]
    for i in range(len(g)):
        if g[i] == 1e9:
            g[i] = 0

    print(*g)
