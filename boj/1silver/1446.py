n, d = map(int, input().split())

graph = [[] for _ in range(d+1)]
for _ in range(n):
    a, b, c = map(int, input().split())
    if b > d: continue
    if b-a < c:
        continue

    graph[a].append((b, c))

from heapq import *

q = []
heappush(q, (0, 0))

for i in range(d):
    graph[i].append((i+1, 1))

distance = [1e9] * (d+1)
distance[0] = 0

while q:
    dist, now = heappop(q)

    if dist > distance[now]:
        continue

    for v, c in graph[now]:
        cost = dist +  c
        if cost < distance[v]:
            distance[v] = cost
            heappush(q, (cost, v))

# print(*distance)
print(distance[d])




