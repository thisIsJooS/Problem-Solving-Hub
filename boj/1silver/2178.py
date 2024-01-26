n, m = map(int, input().split())
graph = [[0] * (m+2)]
for _ in range(n):
    graph.append([0] + list(map(int, list(input()))) + [0])
graph.append([0] * (m+2))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

from collections import deque
q = deque()
q.append((1, 1))

visited = [[False]*(m+2) for _ in range(n+2)]
visited[1][1] = True

while q:
    x, y = q.popleft()
    dist = graph[x][y]
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]

        if graph[nx][ny] and not visited[nx][ny]:
            graph[nx][ny] = dist + 1
            visited[nx][ny] = True
            q.append((nx, ny))


print(graph[n][m])



