from collections import deque

n, m = map(int, input().split())
maps = [list(input()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if maps[i][j] == 'I':
            start = (i, j)
            visited[i][j] = True
            break
    else:
        continue
    break


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

q = deque()
q.append(start)

answer = 0

while q:
    x, y = q.popleft()

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]

        if not (0<=nx<n and 0<=ny<m):
            continue

        if visited[nx][ny]: continue

        if maps[nx][ny] == 'X':
            continue

        if maps[nx][ny] == 'P':
            answer += 1

        q.append((nx, ny))
        visited[nx][ny] = True

print(answer if answer != 0 else 'TT')