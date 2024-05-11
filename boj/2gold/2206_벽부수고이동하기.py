from collections import deque

def solution():
    n, m = map(int, input().split())
    maps = [list(map(int, list(input()))) for _ in range(n)]
    visited = [[[False]*m for _ in range(n)] for _ in range(2)]
    # visited[0] : 부시지 않음
    # visited[1] : 부심

    start = (0, 0, 1, False)
    q = deque([start])
    for i in [0, 1]:
        visited[i][0][0] = True
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    answer = None

    while q:
        x, y, dist, broke = q.popleft()

        if (x, y) == (n-1, m-1):
            answer = dist
            break

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if not (0<=nx<n and 0<=ny<m):
                continue

            if broke:   # 앞에서 이미 부심
                if maps[nx][ny] == 1:
                    continue

                if visited[1][nx][ny]:
                    continue

                visited[1][nx][ny] = True
                q.append((nx, ny, dist+1, broke))

            else:
                if maps[nx][ny] == 1 and not visited[1][nx][ny]:
                    visited[1][nx][ny] = True
                    q.append((nx, ny, dist+1, True))

                elif maps[nx][ny] == 0 and not visited[0][nx][ny]:
                    visited[0][nx][ny] = True
                    q.append((nx, ny, dist+1, False))

    print(answer if answer is not None else -1)

    
solution()