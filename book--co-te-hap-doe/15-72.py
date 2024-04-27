def solution(arr):
    n = len(arr[0])
    dp = [[0] * n for _ in range(4)]

    dp[0][0] = arr[0][0]
    dp[1][0] = arr[1][0]
    dp[2][0] = arr[2][0]
    dp[3][0] = arr[0][0] + arr[2][0]

    for i in range(1, n):
        dp[0][i] = arr[0][i] + max(dp[1][i-1], dp[2][i-1])
        dp[1][i] = arr[1][i] + max(dp[0][i-1], dp[2][i-1], dp[3][i-1])
        dp[2][i] = arr[2][i] + max(dp[0][i-1], dp[1][i-1])
        dp[3][i] = arr[0][i] + arr[2][i] + dp[1][i-1]

    return max(dp[0][-1], dp[1][-1], dp[2][-1], dp[3][-1])

print(solution([[1, 3, 3, 2], [2, 1, 4, 1], [1, 5, 2, 3]]))
print(solution([[1, 7, 13, 2, 6], [2, -4, 2, 5, 4], [5, 3, 5, -3, 1]]))