n = int(input())

prev = None
gap = int(1e9)
gaps = []
arr = []
for i in range(n):
    d = int(input())
    arr.append(d)

    if prev is not None:
        gap = d - prev
        gaps.append(gap)

    prev = d


from math import gcd

prev_gap = gaps[0]
gc = 0
for g in gaps[1:]:
    gc = gcd(prev_gap, g)
    prev_gap = gc


print((arr[-1] - arr[0]) // gc + 1 - n)