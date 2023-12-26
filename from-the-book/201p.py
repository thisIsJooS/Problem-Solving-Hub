n, m = map(int, input().split())
data = list(map(int, input().split()))

start, end = 0, max(data)

res = 0
while start <= end:
    total = 0
    mid = (start + end) // 2

    for x in data:
        if x > mid:
            total += x-mid

    if total < m:
        end = mid-1
    else:
        res = mid
        start = mid + 1

print(res)


"""
4 6 
19 15 10 17
: 15

5 20
4 42 40 26 46
: 36

https://www.acmicpc.net/problem/2805
"""