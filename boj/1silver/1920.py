from bisect import *

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
m = int(input())
cand = list(map(int, input().split()))

for c in cand:
    print(int(bisect_left(arr, c) != bisect_right(arr, c)))