v, e = map(int, input().split())
mat = [[] for _ in range(v+1)]
start = int(input())
for _ in range(e):
    a, b, c = map(int, input().split())
    mat[a].append((b, c))

import heapq
q = []
q.append((0, start))
distance = [1e9] * (v+1)
distance[start] = 0

while q:
    dist, now = heapq.heappop(q)

    if dist > distance[now]:
        continue

    for b, c in mat[now]:
        cost = dist + c
        if cost < distance[b]:
            distance[b] = cost
            heapq.heappush(q, (cost, b))


for d in distance[1:]:
    print('INF' if d == 1e9 else d)
