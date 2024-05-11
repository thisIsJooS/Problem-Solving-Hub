from collections import deque

n = int(input())

maps = [list(input()) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

answer = [0, 0]

visited = [[False]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visited[i][j]:
            continue

        q = deque()
        q.append((i, j))

        value = maps[i][j]

        while q:
            x, y = q.popleft()

            for  k in range(4):
                nx, ny = x+dx[k] , y+dy[k]

                if not (0<=nx<n and 0<=ny<n): continue
                if visited[nx][ny]: continue
                if maps[nx][ny] != value: continue

                visited[nx][ny] = True
                q.append((nx, ny))


        answer[0] += 1


visited = [[False]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visited[i][j]:
            continue

        q = deque()
        q.append((i, j))

        value = maps[i][j]

        while q:
            x, y = q.popleft()

            for  k in range(4):
                nx, ny = x+dx[k] , y+dy[k]

                if not (0<=nx<n and 0<=ny<n): continue
                if visited[nx][ny]: continue

                if value in ['R', 'G']:
                    if maps[nx][ny] == 'B':
                        continue
                else:
                    if maps[nx][ny] != value:
                        continue

                visited[nx][ny] = True
                q.append((nx, ny))


        answer[1] += 1


print(*answer)
