import sys, heapq
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    q = []
    for a in arr:
        heapq.heappush(q, a)

    res = 0
    while len(q) > 1:
        a, b = heapq.heappop(q), heapq.heappop(q)
        agg = a + b
        heapq.heappush(q, agg)
        res += agg

    print(res)