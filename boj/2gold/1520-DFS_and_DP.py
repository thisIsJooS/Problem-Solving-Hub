import sys
input = sys.stdin.readline

N, M = map(int, input().split())
INF = 1e9
graph = [list(map(int, input().split())) for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

dp = [[-1] * M for _ in range(N)]

def f(x, y):
    if x == N-1 and y == M-1:
        return 1

    if dp[x][y] > -1:
        return dp[x][y]

    dp[x][y] = 0
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if not (0<=nx<N and 0<=ny<M):
            continue

        if graph[nx][ny] >= graph[x][y]:
            continue

        dp[x][y] += f(nx, ny)

    return dp[x][y]


print(f(0, 0))