n, m = map(int, input().split())
arr = list(map(int, input().split()))

if sum(arr) < m:
    print(0)
    exit(0)

start = 0
end = max(arr)
ans = end

while start <= end:
    mid = (start + end) // 2
    res = 0
    for a in arr:
        if a > mid:
            res += a - mid

    if res < m:
        end = mid - 1
    else:
        ans = mid
        start = mid + 1

print(ans)