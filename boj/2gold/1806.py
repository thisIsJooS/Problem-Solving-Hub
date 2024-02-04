n, s = map(int, input().split())
arr = list(map(int, input().split()))

end = 0
ans = 1e9
total = 0

for start in range(n):
    while end < n and total < s:
        total += arr[end]
        end += 1


    if total >= s:
        ans = min(ans, end-start)
    total -= arr[start]

print(ans if ans < 1e9 else 0)

