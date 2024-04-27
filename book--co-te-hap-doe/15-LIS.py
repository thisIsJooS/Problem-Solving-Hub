arr = [1, 4, 2, 3, 1, 5, 7, 3]

dp = [1] * len(arr)

for i in range(len(arr)):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(*dp)

