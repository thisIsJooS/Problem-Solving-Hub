# https://school.programmers.co.kr/learn/courses/30/lessons/42897

def solution(money):
    answer = 0

    n = len(money)

    dp = [[0] * n for _ in range(2)]
    # 0행 : 첫 집을 안 간 경우
    # 1행 : 첫 집을 간 경우

    dp[0][0] = 0
    dp[1][0] = money[0]

    dp[0][1] = money[1]
    dp[1][1] = money[0]

    for i in range(2):
        for j in range(2, n):
            if j != n - 1 or i == 0:
                dp[i][j] = max(dp[i][j - 1], dp[i][j - 2] + money[j])
            else:
                dp[i][j] = dp[i][j - 1]

    return max(dp[0][n - 1], dp[1][n - 1])