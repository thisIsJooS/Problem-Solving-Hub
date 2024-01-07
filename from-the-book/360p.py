import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

res = 0
for a in arr:
    res += abs(a - arr[n//2])

mid = n//2
min_index = mid
def f(start, end):
    global res, min_index

    for i in range(mid+1, n):
        val = 0
        for a in arr:
            val += abs(a - arr[i])
        if val < res:
            res = val
            min_index = i
        else:
            break

    for i in range(mid-1, -1, -1):
        val = 0
        for a in arr:
            val += abs(a - arr[i])
        if val <= res:
            res = val
            min_index = i
        else:
            break


f(0, n-1)
print(arr[min_index])


