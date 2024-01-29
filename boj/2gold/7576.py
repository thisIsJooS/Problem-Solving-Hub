from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]


def already():
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                return False
    return True

if already():
    print(0)
    exit(0)

q = deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append((i, j, 0))


while q:
    x, y, d = q.popleft()

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if not (0<=nx<n and 0<=ny<m):
            continue

        if graph[nx][ny] == 0:
            graph[nx][ny] = d+1
            q.append((nx, ny, d+1))


def f():
    cnt = 0

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                return -1
            cnt = max(cnt, graph[i][j])

    return cnt

print(f())

