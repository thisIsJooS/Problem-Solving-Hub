import heapq
import sys
input = sys.stdin.readline

n = int(input())
q = []

for _ in range(n):
    heapq.heappush(q, int(input()))

res = 0
while q:
    if len(q) >= 2:
        a, b = heapq.heappop(q), heapq.heappop(q)
        res += a+b
        heapq.heappush(q, a+b)
    else:
        break

print(res)