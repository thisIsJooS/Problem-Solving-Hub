n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))


dp = [0] * n
def f():
    dp[0] = arr[0]
    if n<=1 : return
    dp[1] = arr[0] + arr[1]
    if n<=2 : return

    for i in range(2, n):
        dp[i] = max(dp[i-2] + arr[i], dp[i-3]+arr[i-1]+arr[i])

f()
print(dp[n-1])