import math
import sys
input = sys.stdin.readline
#
start, end = map(int, input().split())
arr = [True] * (end - start + 1)
cnt = 0

for i in range(2, int(math.sqrt(end))+1):
    p = i*i

    iter_start = p-(start%p)
    if start % p == 0:
        iter_start = 0

    for j in range(iter_start, end-start+1, p):
        if arr[j]:
            arr[j] = False
            cnt += 1


print(end-start+1-cnt)



