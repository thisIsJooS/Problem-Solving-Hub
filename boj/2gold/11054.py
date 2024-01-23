n = int(input())

arr = list(map(int, input().split()))
arr_rev = arr[::-1]
dp = [1]*n
dp_rev = [1]*n

for i in range(n):
    for j in range(i):
        if arr[j] < arr[i] and dp[j] >= dp[i]:
            dp[i] = dp[j] + 1

        if arr_rev[j] < arr_rev[i] and dp_rev[j] >= dp_rev[i]:
            dp_rev[i] = dp_rev[j] + 1

dp_rev = dp_rev[::-1]

res = []
for i in range(n):
    res.append(dp[i] + dp_rev[i])


print(max(res)-1)