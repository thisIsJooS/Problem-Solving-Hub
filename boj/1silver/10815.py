input()
a = list(map(int, input().split()))
input()
b = list(map(int, input().split()))


a.sort()
from bisect import *

for c in b:
    if bisect_left(a, c) == bisect_right(a, c):
        print(0, end = ' ')
    else:
        print(1, end = ' ')