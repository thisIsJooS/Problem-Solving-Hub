from collections import deque


def solution():
    m, n = map(int, input().split())
    maps = [list(map(int, list(input()))) for _ in range(n)]

    start = (0, 0)
    q = deque()
    q.append((0, 0))  # x, y, 이동 거리, 부신 개수

    visited = [[None] * m for _ in range(n)]
    visited[0][0] = (0, 0)      # 이동 거리, 부신 개수
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

    while q:
        x, y = q.popleft()
        d, b = visited[x][y][0], visited[x][y][1]

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if not (0<=nx<n and 0<=ny<m):
                continue

            if visited[nx][ny] is None:
                if maps[nx][ny] == 1:
                    visited[nx][ny] = (d+1, b+1)
                else:
                    visited[nx][ny] = (d+1, b)
                q.append((nx, ny))
                continue

            nd, nb = visited[nx][ny][0], visited[nx][ny][1]

            if maps[nx][ny] == 1:
                if nb > b+1:
                    visited[nx][ny] = (d+1, b+1)
                    q.append((nx, ny))
            else:
                if nb > b:
                    visited[nx][ny] = (d+1, b)
                    q.append((nx, ny))

    print(visited[n-1][m-1][1])

solution()

