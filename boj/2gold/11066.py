import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    dp = [[0]*n for _ in range(n)]

    total = [[0] * n for _ in range(n)]
    for i in range(n):
        total[i][i] = arr[i]

    for i in range(n):
        for j in range(i + 1, n):
            total[i][j] = total[i][j - 1] + arr[j]

    for i in range(n-1):
        dp[i][i+1] = arr[i] + arr[i+1]

    for k in range(2, n):
        for i in range(n-k):
            min_val = min(dp[i][j] + dp[j+1][i+k] + total[i][i+k] for j in range(i, i+k))

            dp[i][i+k] = min_val

    print(dp[0][n-1])