"""
일직선
입접한 칸이 공격받으면 알 수 있음
들키지 않기 위해 최소한 한 칸 이상 떨어진 창고 약탈

1 3 1 5 -> 2번째와 4번째 했을 때 총 8개로 최대 가능
식량의 최대 값은?
"""

n = int(input())

data = list(map(int, input().split()))

dp = [-1] * n
dp[0] = data[0]
dp[1] = max(data[0], data[1])

for i in range(2, n):
    dp[i] = max(dp[i-1], dp[i-2]+data[i])

print(dp[n-1])

