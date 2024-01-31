t = int(input())

def f():
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(2)]

    if n == 1:
        return max(map(max, arr))

    dp = [[0]*n for _ in range(2)]
    for i in [0, 1]:
        dp[i][0] = arr[i][0]

    for i in [0, 1]:
        dp[i][1] = arr[1-i][0] + arr[i][1]

    if n == 2:
        return max(map(max, dp))

    for j in [2]:
        dp[0][j] = max(dp[0][j-2] + arr[1][j-1] + arr[0][j], dp[1][j-2] + arr[0][j])
        dp[1][j] = max(dp[1][j-2] + arr[0][j-1] + arr[1][j], dp[0][j-2] + arr[1][j])

    for j in range(3, n):
        dp[0][j] = max(dp[1][j-2], dp[1][j-1]) + arr[0][j]
        dp[1][j] = max(dp[0][j-2], dp[0][j-1]) + arr[1][j]

    # print(*dp, sep='\n')
    return max(map(max, dp))

for _ in range(t):
    print(f())
