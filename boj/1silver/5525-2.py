n = int(input())
m = int(input())
s = input()

dp = [0] * m
p = 'IO' * n + 'I'

for i in range(m):
    if s[i] == 'O':
        continue

    # s[i] == 'I' 일 경우
    if i <= 1:
        dp[i] = 1
        continue

    if dp[i-2] and not dp[i-1]:
        dp[i] = dp[i-2] + 2
    else:
        dp[i] = 1

cnt = 0
for val in dp:
    if val >= 2*n+1:
        cnt += 1

print(cnt)
