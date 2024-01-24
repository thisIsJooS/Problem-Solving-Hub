import sys
input = sys.stdin.readline

k, n = map(int, input().split())
arr = [int(input()) for _ in range(k)]

start = 1
end = max(arr)

def get(arr, mid):
    res = 0
    for a in arr:
        res += a // mid
    return res


res = 0
while start <= end:
    mid = (start + end) // 2
    if mid == 0:
        break

    if get(arr, mid) >= n:
       res = max(res, mid)
       start = mid + 1
    elif get(arr, mid) < n:
        end = mid - 1

print(res)