from bisect import *

N, H = map(int, input().split())

arr = []
for _ in range(N):
    arr.append(int(input()))

down, up = [], []

for i, e in enumerate(arr):
    if i % 2 == 0:
        down.append(e)
    else:
        up.append(e)

down.sort()
up.sort()

ans = 1e9
count = 1

for h in range(1, H+1):
    cnt1 = bisect_left(down, h)
    cnt1 = N//2 - cnt1

    cnt2 = bisect_right(up, H - h)
    cnt2 = N//2 - cnt2

    val = cnt1 + cnt2

    if val < ans:
        ans = val
        count = 1
    elif val == ans:
        count += 1

print(ans, count)
