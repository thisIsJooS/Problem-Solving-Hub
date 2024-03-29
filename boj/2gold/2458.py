import sys
input  = sys.stdin.readline

v, e = map(int, input().split())
graph = [[1e9] *(v+1) for _ in range(v+1)]

for _ in range(e):
    a, b= map(int, input().split())
    graph[a][b] = 1

for i in range(v+1):
    graph[i][i] = 0

for k in range(1, v+1):
    for i in range(1, v+1):
        for j in range(1, v+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

ans = 1e9
cnt = 0
for i in range(1, v+1):
    for j in range(1, v+1):
        if graph[i][j] == 1e9 and graph[j][i] == 1e9:
            break

    else:
        cnt += 1


print(cnt)