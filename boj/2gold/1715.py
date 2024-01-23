import sys, heapq
input = sys.stdin.readline
q = []
for _ in range(int(input())):
    n = int(input())
    q.append(n)

heapq.heapify(q)

res = 0
while len(q) > 1:
    a, b = heapq.heappop(q), heapq.heappop(q)
    agg = a + b
    heapq.heappush(q, agg)
    res += agg

print(res)