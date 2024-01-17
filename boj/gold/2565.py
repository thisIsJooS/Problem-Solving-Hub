arr = []
n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))

arr.sort(key = lambda x: x[0])

for i in range(n):
    arr[i] = arr[i][1]


dp = [1] * n

for i in range(n):
    for j in range(i):
        if arr[j] < arr[i] and dp[j] >= dp[i]:
            dp[i] = dp[j] + 1

print(n - max(dp))