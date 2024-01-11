n = int(input())
arr = [0]
dp = [0] * (n+2)
for _ in range(n):
    t, p = map(int, input().split())
    arr.append((t, p))


for i in range(1, n+1):
    t, p = arr[i]

    for j in range(i+t, n+2):
        dp[j] = max(dp[j], dp[i]+p)


print(max(dp))




