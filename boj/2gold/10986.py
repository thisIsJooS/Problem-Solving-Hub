import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [0] + list(map(int, input().split()))

brr = [0] * M

for i in range(N+1):
    arr[i] += arr[i-1]
    arr[i] = arr[i] % M

    brr[arr[i]] += 1



import math
res = 0
for b in brr:
    res += math.comb(b, 2)


print(res)








