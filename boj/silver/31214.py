arr = list(map(int, input().split()))
k = int(input())

start = 0
end = max(arr)

res = 0
while start <= end:
    total = 0
    mid = (start + end) // 2

    for x in arr:
        if x > mid:
            total += x - mid

    if total > k:
        start = mid + 1
    else:
        end = mid - 1
        res = mid

print(res)