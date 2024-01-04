from collections import deque

N, K = map(int, input().split())
graph = []
data = []
for i in range(N):
    graph.append(list(map(int, input().split())))
    for j in range(N):
        if graph[i][j] != 0:
            data.append((graph[i][j], 0, i, j))     # (바이러스 종류, 시간, 위치X, 위치Y)

data.sort()
q = deque(data)

S, X, Y = map(int, input().split())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

while q:
    virus, s, x, y = q.popleft()

    if s == S:
        break

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if not (0<=nx<N and 0<=ny<N):
            continue

        if graph[nx][ny] == 0:
            graph[nx][ny] = virus
            q.append((virus, s+1, nx, ny))

print(graph[X-1][Y-1])