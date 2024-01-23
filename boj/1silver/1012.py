from collections import deque


def is_valid(nx, ny, m, n):
    if not 0 <= nx < m or not 0 <= ny < n:
        return False
    return True


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    for __ in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1

    res = 0
    q = deque()
    for i in range(N):
        for j in range(M):
            if visited[i][j]: continue
            if graph[i][j] == 1:
                res += 1
                visited[i][j] = True
                q.append((i, j))

                while q:
                    x, y = q.popleft()

                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]
                        if not is_valid(ny, nx , M, N):
                            continue
                        if not visited[nx][ny] and graph[nx][ny]:
                            q.append((nx, ny))
                            visited[nx][ny] = True

    print(res)




