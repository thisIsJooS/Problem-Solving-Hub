import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

dp = [[-1]*n for _ in range(n)]

def f(x, y):
    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = 1

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if not (0<=nx<n and 0<=ny<n): continue
        if graph[nx][ny] <= graph[x][y]: continue

        dp[x][y] = max(f(nx, ny)+1, dp[x][y])

    return dp[x][y]

for i in range(n):
    for j in range(n):
        f(i, j)

# print(*dp, sep='\n')
print(max(map(max, dp)))