import sys
input = sys.stdin.readline
from heapq import *

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


dp = [None] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())

    if dp[a] is not None:
        print(dp[a][b])
        continue

    if dp[b] is not None:
        print(dp[b][a])
        continue

    q = []
    heappush(q, (0, a))
    distance = [1e9] * (n+1)
    distance[a] = 0

    while q:
        dist, now = heappop(q)

        if dist > distance[now]:
            continue

        for v, c in graph[now]:
            cost = dist + c
            if cost < distance[v]:
                distance[v] = cost
                heappush(q, (cost, v))

    dp[a] = distance
    print(distance[b])
