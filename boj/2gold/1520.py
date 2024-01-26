import sys
input = sys.stdin.readline
from heapq import *

N, M = map(int, input().split())
INF = 1e9
graph = [list(map(int, input().split())) for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

dp = [[0] * M for _ in range(N)]
dp[0][0] = 1
q = []
heappush(q, (-graph[0][0], 0, 0))

while q:
    val, x, y = heappop(q)

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if not (0<=nx<N and 0<=ny<M):
            continue

        if graph[nx][ny] >= graph[x][y]:
            continue

        if dp[nx][ny] == 0:     # 방문한 적이 없다면,
            heappush(q, (-graph[nx][ny], nx, ny))

        dp[nx][ny] += dp[x][y]

print(dp[N-1][M-1])




