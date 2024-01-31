n = int(input())
damage = [0] + list(map(int, input().split()))
hp = [0] + list(map(int, input().split()))

dp = [[0]*100 for _ in range(n+1)]

for i in range(1, n+1):
    for d in range(100):
        if damage[i] > d:
            dp[i][d] = dp[i-1][d]
        else:
            val_with = hp[i] + dp[i-1][d-damage[i]]
            val_without = dp[i-1][d]

            dp[i][d] = max(val_with, val_without)

# print(*dp, sep='\n')
print(max(map(max, dp)))