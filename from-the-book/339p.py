import sys
input = sys.stdin.readline

N, M, K, start = map(int, input().split())
graph = [[] for _ in range(N+1)]
distance = [int(1e9)] * (N+1)
distance[start] = 0

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

import heapq
q = []
heapq.heappush(q, (0, start))

while q:
    dist, now = heapq.heappop(q)

    if distance[now] < dist:
        continue

    for v in graph[now]:
        cost = dist + 1
        if cost < distance[v]:
            distance[v] = cost
            heapq.heappush(q, (cost, v))


def f():
    if K not in distance:
        print(-1)
        return

    for i in range(1, N+1):
        if distance[i] == K:
            print(i)

f()
