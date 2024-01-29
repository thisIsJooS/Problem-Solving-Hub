from heapq import *
import sys

input = sys.stdin.readline

start, end = map(int, input().split())

distance = [1e9] * 100001

distance[start] = 0
q = []
heappush(q, (0, start))

ans = None

while q:
    dist, now = heappop(q)

    if now == end:
        ans = dist
        break

    if dist > distance[now]:
        continue

    for v, c in [(now-1, 1), (now+1, 1), (now*2, 0)]:
        if not (0<=v<=100000):
            continue

        cost = dist + c
        if cost < distance[v]:
            distance[v] = cost
            heappush(q, (cost, v))


print(ans)


