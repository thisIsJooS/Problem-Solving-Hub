from heapq import heappush, heappop
from collections import defaultdict

v, e = map(int, input().split())
graph = defaultdict(list)

gender = [0] + list(input().split())

for _ in range(e):
    a, b, c = map(int, input().split())

    if gender[a] == gender[b]:
        continue

    graph[a].append((b, c))
    graph[b].append((a, c))

q = []
heappush(q, (0, 1))
visited = set()
res = 0

while q:
    cost, now = heappop(q)

    if now in visited:
        continue

    visited.add(now)
    res += cost

    for b, c in graph[now]:
        heappush(q, (c, b))

if len(visited) != v:
    print(-1)
else:
    print(res)