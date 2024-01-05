from collections import deque
import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

N, L, R = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(N)]

union_num = 0
time = -1


while union_num != N*N:
    time += 1
    union = [[-1]*N for _ in range(N)]
    union_coords = [[] for _ in range(N * N)]
    union_sums = [0] * (N * N)
    union_counts = [0] * (N * N)
    union_num = 0

    for i in range(N):
        for j in range(N):
            if union[i][j] != -1: continue
            q = deque()
            q.append((i, j))
            union[i][j] = union_num
            union_coords[union_num].append((i, j))
            union_sums[union_num] += mat[i][j]
            union_counts[union_num] += 1

            while q:
                x, y = q.popleft()
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if not (0<=nx<N and 0<=ny<N): continue
                    if union[nx][ny] != -1: continue
                    if L <= abs(mat[x][y] - mat[nx][ny]) <= R:
                        union[nx][ny] = union_num
                        union_coords[union_num].append((nx, ny))
                        union_sums[union_num] += mat[nx][ny]
                        union_counts[union_num] += 1
                        q.append((nx, ny))

            union_num += 1

    # 인구 재분배
    for i in range(N*N):
        summary, count = 0, 0
        for coord in union_coords[i]:
            x, y = coord
            val = union_sums[i] // union_counts[i]
            mat[x][y] = val


print(time)