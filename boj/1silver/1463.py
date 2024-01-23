n = int(input())
if n==1:
    print(0)
    exit(0)
dp = [1e9]*(3*(n-1)+1)
dp[n] = 0

for i in range(n-1, 0, -1):
    dp[i] = min(dp[i+1], dp[i*3], dp[i*2]) + 1

print(dp[1])