import sys
input = sys.stdin.readline

n, c = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort()

length = arr[-1] - arr[0]
max_gap = length // (c-1)


def f(start, end):
    res = 0
    while start <= end:
        mid = (start + end) // 2

        if arr[mid]-arr[0] <= max_gap:
            res = max(res, arr[mid]-arr[0])
            start = mid + 1
        elif arr[mid]-arr[0] > max_gap:
            end = mid - 1

    return res

print(f(0, n-1))