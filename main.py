n, k = map(int, input().split())

factorial = [1, 1]

mod = 1000000007

i = 2
while len(factorial) <= 4000000:
    factorial.append((i * factorial[-1]) % mod)
    i += 1

res = factorial[n] // (factorial[k] * factorial[n-k])
print(res % mod)
