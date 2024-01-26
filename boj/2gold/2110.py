import sys
input = sys.stdin.readline

def is_valid(arr, size):
    global m
    cnt = 1
    prev = arr[0]
    for i in range(len(arr)):
        if arr[i] - prev < size:
            continue
        else:
            prev = arr[i]
            cnt += 1

    if cnt >= m:
        return True
    else:
        return False


n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))

arr.sort()
start, end = 0, arr[-1] - arr[0]

ans = 0
while start <= end:
    mid = (start + end) // 2
    if not is_valid(arr, mid):
        end = mid - 1
    else:
        start = mid + 1
        ans = mid

print(ans)