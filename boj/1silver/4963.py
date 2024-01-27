dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, -1, 1, -1, 1]

from collections import deque

def f(arr):
    n = len(arr)
    m = len(arr[0])
    cnt = 0
    visited = [[False]*m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if arr[i][j] and not visited[i][j]:
                q = deque()
                q.append((i, j))
                visited[i][j] = True

                while q:
                    x, y = q.popleft()

                    for k in range(8):
                        nx, ny = x+dx[k], y+dy[k]
                        if not (0<=nx<n and 0<=ny<m):
                            continue

                        if visited[nx][ny]:
                            continue

                        if arr[nx][ny]:
                            q.append((nx, ny))
                            visited[nx][ny] = True

                cnt += 1

    return cnt


while True:
    n, m = map(int, input().split())

    if (n, m) == (0, 0):
        exit(0)

    graph = [list(map(int, input().split())) for _ in range(m)]
    print(f(graph))

