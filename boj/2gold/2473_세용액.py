n = int(input())
arr = list(map(int, input().split()))

arr.sort()

"""
3개를 섞어서 합이 0에 제일 가까운거 
"""

res = None
val = 1e10

for i in range(n-2):
    start = i+1
    end = n-1

    while start < end:
        agg = arr[i] + arr[start] + arr[end]

        if abs(agg) < val:
            val = abs(agg)
            res = (arr[i], arr[start], arr[end])

        if agg < 0:
            start += 1
        elif agg > 0:
            end -= 1
        else:
            break

print(*res)


