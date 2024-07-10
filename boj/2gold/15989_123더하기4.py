dp = [[0]*4 for _ in range(10_001)]

dp[1] = [0, 1, 0, 0]
dp[2] = [0, 1, 1, 0]
dp[3] = [0, 2, 0, 1]

for i in range(4, 10001):
    dp[i][1] = sum(dp[i-1])
    dp[i][2] = sum(dp[i-2][2:])
    dp[i][3] = dp[i-3][3]

for _ in range(int(input())):
    a = int(input())
    print(sum(dp[a]))