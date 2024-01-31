from collections import deque
import sys
input = sys.stdin.readline

m, n, H = map(int, input().split())
mat = []
for _ in range(H):
    f = [list(map(int, input().split())) for _ in range(n)]
    mat.append(f)


def is_already():
    for f in range(H):
        for i in range(n):
            for j in range(m):
                if mat[f][i][j] == 0:
                    return False

    return True


if is_already():
    print(0)
    exit()


dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

for f in range(H):
    for i in range(n):
        for j in range(m):
            if mat[f][i][j] == 1:
                q = deque()
                q.append((2, f, i, j))
                mat[f][i][j] = 2

                while q:
                    cnt, h, x, y = q.popleft()

                    for k in range(6):
                        nh, nx, ny = h+dz[k], x + dx[k], y + dy[k]
                        if not (0<=nh<H and 0<=nx<n and 0<=ny<m):
                            continue

                        if mat[nh][nx][ny] != -1:
                            if mat[nh][nx][ny] == 0:
                                mat[nh][nx][ny] = cnt + 1
                                q.append((cnt + 1, nh, nx, ny))

                            elif mat[nh][nx][ny] > cnt + 1:
                                mat[nh][nx][ny] = cnt + 1
                                q.append((cnt+1, nh, nx, ny))



def is_fail():
    for f in range(H):
        for i in range(n):
            for j in range(m):
                if mat[f][i][j] == 0:
                    return True
    return False



if is_fail():
    print(-1)
    exit(0)

ans = 0
for f in range(H):
    for i in range(n):
        for j in range(m):
            ans = max(ans, mat[f][i][j])



print(ans-2)
