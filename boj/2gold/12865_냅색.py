N, K = map(int, input().split())

weight = [0]
value = [0]

for _ in range(N):
    w, v = map(int, input().split())
    weight.append(w)
    value.append(v)

dp = [[0]*(K+1) for _ in range(N+1)]

for i in range(1, N+1):
    for w in range(1, K+1):
        if weight[i] > w:
            dp[i][w] = dp[i-1][w]

        else:
            val_with = value[i] + dp[i-1][w-weight[i]]
            val_without = dp[i-1][w]

            dp[i][w] = max(val_without, val_with)

print(dp[N][K])


