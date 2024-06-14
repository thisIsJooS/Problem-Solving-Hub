n = int(input())

arr = [[0] + list(map(int, input().split())) + [0] for _ in range(n)]

max_res, min_res = None, None

dp = [[0] * 5 for _ in range(2)]
d = 1
for i in range(n):
    for j in range(1, 4):
        dp[d][j] = max(dp[1-d][j-1], dp[1-d][j], dp[1-d][j+1]) + arr[i][j]
    d = 1-d

max_res = max(dp[1-d])

for i in range(n):
    for j in [0, -1]:
        arr[i][j] = 1e9

dp = [[1e9] * 5 for _ in range(2)]
d = 1
dp[0] = arr[0][:]
for i in range(1, n):
    for j in range(1, 4):
        dp[d][j] = min(dp[1-d][j-1], dp[1-d][j], dp[1-d][j+1]) + arr[i][j]
    d = 1-d

min_res = min(dp[1-d])



print(max_res, min_res)