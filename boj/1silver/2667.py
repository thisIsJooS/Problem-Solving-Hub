order = 0
n = int(input())
graph = [list(map(int, list(input()))) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

res = [0] * (n**2)

from collections import deque

for i in range(n):
    for j in range(n):
        if not graph[i][j]: continue

        q = deque()
        q.append((i, j))
        graph[i][j] = 0
        res[order] += 1

        while q:
            x, y = q.popleft()
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if not (0<=nx<n and 0<=ny<n): continue
                if graph[nx][ny]:
                    res[order] += 1
                    q.append((nx, ny))
                    graph[nx][ny] = 0

        order += 1

res = res[:order]
res.sort()
print(order)
print(*res, sep='\n')