import sys
input = sys.stdin.readline

n, m = map(int, input().split())

mat = [list(map(int, input().split())) for _ in range(n)]

from collections import deque
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


order = 2
ans = 0
for i in range(n):
    for j in range(m):
        if mat[i][j] == 1:
            mat[i][j] = order

            q = deque()
            q.append((i, j))
            cnt = 1

            while q:
                x, y = q.popleft()
                for k in range(4):
                    nx, ny = x+dx[k], y+dy[k]
                    if not(0<=nx<n and 0<=ny<m):
                        continue

                    if mat[nx][ny] == 1:
                        mat[nx][ny] = order
                        q.append((nx, ny))
                        cnt += 1

            ans = max(ans, cnt)
            order += 1


print(order-2)
print(ans)





