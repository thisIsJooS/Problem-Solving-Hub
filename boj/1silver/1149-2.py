import sys
input = sys.stdin.readline

n = int(input())
datas = [list(map(int, input().split())) for _ in range(n)]
dp = [[0, 0, 0] for _ in range(n)]

for i in range(3):
    dp[0][i] = datas[0][i]


for i in range(1, n):
    # R
    if dp[i-1][1] < dp[i-1][2]:
        dp[i][0] = datas[i][0] + dp[i-1][1]
    else:
        dp[i][0] = datas[i][0] + dp[i-1][2]

    # G
    if dp[i-1][0] < dp[i-1][2]:
        dp[i][1] = datas[i][1] + dp[i-1][0]
    else:
        dp[i][1] = datas[i][1] + dp[i-1][2]

    # B
    if dp[i-1][1] < dp[i-1][0]:
        dp[i][2] = datas[i][2] + dp[i-1][1]
    else:
        dp[i][2] = datas[i][2] + dp[i-1][0]

print(min(dp[n-1]))
