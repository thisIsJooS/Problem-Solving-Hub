from heapq import *

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())

distance = [1e9] * (n+1)
distance[start] = 0
q = []
heappush(q, (0, start))

while q:
    dist, now = heappop(q)

    if dist > distance[now]:
        continue

    for v, c in graph[now]:
        cost = dist + c
        if cost < distance[v]:
            distance[v] = cost
            heappush(q, (cost, v))

print(distance[end])