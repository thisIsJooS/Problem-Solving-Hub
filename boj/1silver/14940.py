from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def get_dest():
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                return (i, j)

x, y = get_dest()
q = deque()
q.append((x, y))

res = [[-1]*m for _ in range(n)]
res[x][y] = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            res[i][j] = 0

while q:
    x, y = q.popleft()
    now = res[x][y]

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if not (0<=nx<n and 0<=ny<m):
            continue

        if res[nx][ny] == -1:
            res[nx][ny] = now + 1
            q.append((nx, ny))

for r in res:
    print(*r)



