from heapq import *
import sys
input = sys.stdin.readline

n, e = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


def get_min_dist(start, end):
    global n
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


    return distance[end]


u, v = map(int, input().split())
a = get_min_dist(1, u) + get_min_dist(u, v) + get_min_dist(v, n)
b = get_min_dist(1, v) + get_min_dist(v, u) + get_min_dist(u, n)

ans = min(a, b)
print(ans if ans < 1e9 else -1)

