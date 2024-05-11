n = int(input())

dp = [0] * 50001

for i in range(1, int(50001**0.5)+1):
    dp[i*i] = 1

dp[2] = 2
dp[3] = 3

if n <= 4:
    print(dp[n])
    exit(0)

for i in range(4, n+1):
    if dp[i] == 1:
        continue

    val = 1e9
    p = 1
    while i - p**2 > 0:
        val = min(val, dp[i-p**2] + 1)
        p += 1

    dp[i] = val

print(dp[n])