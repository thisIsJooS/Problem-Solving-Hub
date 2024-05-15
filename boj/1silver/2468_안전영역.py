from collections import deque

def solution():
    n = int(input())

    maps = [list(map(int, input().split())) for _ in range(n)]
    answer = 0
    for h in range(101):
        answer = max(answer, f(maps, h))

    print(answer)




def f(maps, h):
    n = len(maps)

    board = [[True] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if maps[i][j] <= h:
                board[i][j] = False

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    visited = [[False] * n for _ in range(n)]
    cnt = 0

    for i in range(n):
        for j in range(n):
            if visited[i][j]: continue

            if not board[i][j]: continue

            visited[i][j] = True

            q = deque()
            q.append((i, j))

            while q:
                x, y = q.popleft()

                for p in range(4):
                    nx, ny = x+dx[p], y+dy[p]
                    if not (0<=nx<n and 0<=ny<n): continue
                    if visited[nx][ny]: continue
                    if not board[nx][ny]: continue

                    visited[nx][ny] = True
                    q.append((nx, ny))

            cnt += 1

    return cnt


solution()
