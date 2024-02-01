import sys
input  = sys.stdin.readline

v, e = map(int, input().split())
graph = [[1e9] *(v+1) for _ in range(v+1)]

for _ in range(e):
    a, b, c= map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c

for i in range(v+1):
    graph[i][i] = 0

for k in range(1, v+1):
    for i in range(1, v+1):
        for j in range(1, v+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

ans = 1e9
g = None
import statistics as st
for i in range(1, v+1):
    mean = st.mean(graph[i])
    if mean < ans:
        g = i
        ans = mean


print(g)