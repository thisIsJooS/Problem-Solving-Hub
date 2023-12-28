"""
각 통로는 단방향
C 에서 출발하여 퍼져나감
받을 도시는 몇 개? 그리고 받는데까지 걸리는 시간은?
"""
import heapq

n, m, start = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y, z = map(int, input().split()) # x에서 y까지 이어지는 통로, 시간은 z
    graph[x].append((y, z))

INF = int(1e9)
distance = [INF] * (n+1)
distance[start] = 0

q = []
heapq.heappush(q, (0, start))

while q:
    dist, now = heapq.heappop(q)
    if dist > distance[now]:
        continue

    for i in graph[now]:
        cost = dist + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))

cnt, time = 0, 0
for i in range(1, n+1):
    if distance[i] != INF:
        cnt += 1
        time = max(time, distance[i])

print(cnt-1, time)

"""
3 2 1
1 2 4
1 3 2
"""



