from collections import defaultdict
from heapq import heappush, heappop

v, e = map(int, input().split())

graph = defaultdict(list)
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

distance = [int(1e9)] * (v+1)
distance[1] = 0
q = []
heappush(q, (0, 1))

while q:
    dist, now = heappop(q)

    if distance[now] < dist:
        continue

    for b, c in graph[now]:
        cost = distance[now] + c
        if distance[b] > cost:
            distance[b] = cost
            heappush(q, (cost, b))

print(distance[v])