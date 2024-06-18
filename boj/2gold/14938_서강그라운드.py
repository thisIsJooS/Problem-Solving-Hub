n, m ,r = map(int, input().split())
items = [0] + list(map(int, input().split()))
graph = [[1e9] * (n+1) for _ in range(n+1)]
for i in range(n+1):
    graph[i][i] = 0

for _ in range(r):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c

for k in range(1, n+1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

res = 0
for i in range(1, n+1):
    val = 0
    for j in range(1, n+1):
        if graph[i][j] <= m:
            val += items[j]

    res = max(res, val)

print(res)
