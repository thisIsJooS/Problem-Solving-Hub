n, m, k = map(int, input().split())

maps = [[0]*m for _ in range(n)]
for _ in range(k):
    a, b, c, d = map(int, input().split())

    for i in range(a, c):
        for j in range(b, d):
            maps[j][i] = 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
from collections import deque
res = []

for i in range(n):
    for j in range(m):
        if maps[i][j] != 0:
            continue

        q = deque()
        q.append((i, j))
        maps[i][j] = 2
        cnt = 1
        while q:
            x, y = q.popleft()

            for k in range(4):
                nx, ny = x+dx[k], y+dy[k]

                if not (0<=nx<n and 0<=ny<m):
                    continue

                if maps[nx][ny] != 0:
                    continue

                maps[nx][ny] = 2
                q.append((nx, ny))
                cnt += 1

        res.append(cnt)

print(len(res))
print(*sorted(res))
