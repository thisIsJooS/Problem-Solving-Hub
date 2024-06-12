from collections import defaultdict
from heapq import heappop, heappush

N = int(input())
M = int(input())
graph = defaultdict(list)
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start_point, end_point = map(int, input().split())

distance = [1e9] * (N+1)
distance[start_point] = 0
q = []
heappush(q, (0, start_point, [start_point]))


# 경로 추적을 위한 배열
route = [-1] * (N+1)
route[start_point] = start_point        # 도착지점은 자기자신

while q:
    dist, now, path = heappop(q)

    if distance[now] < dist:
        continue

    for b, c in graph[now]:
        cost = c + dist
        if distance[b] > cost:
            distance[b] = cost
            route[b] = now         # 이전 정점 기억
            heappush(q, (cost, b, path + [b]))

cnt = 0
path = []
def trace(node):
    global cnt
    cnt += 1
    if route[node] == node:
        path.append(node)
        return
    trace(route[node])
    path.append(node)

trace(end_point)
print(distance[end_point])
print(cnt)
print(*path)