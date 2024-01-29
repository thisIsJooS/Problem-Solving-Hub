n, m = map(int, input().split())

graph = [[100]*(n+1) for _ in range(n+1)]
for i in range(n+1):
    graph[i][i] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


ans, total = None, 1e9
for i in range(1, n+1):
    agg = sum(graph[i])
    if total > agg:
        ans = i
        total = agg

print(ans)

