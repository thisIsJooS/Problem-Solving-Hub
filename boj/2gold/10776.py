import heapq

H, N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, t, h = map(int, input().split())
    graph[a].append((b, t, h))  # 목적지, 시간, 깎이는 두께
    graph[b].append((a, t, h))

start, end = map(int, input().split())

distance = [[1e9]*(H+1) for _ in range(N+1)]
distance[start][H] = 0

q = []
heapq.heappush(q, (0, start, H))    # 시간, 정점, 현재 두께
ans = None

while q:
    dist, now, height = heapq.heappop(q)

    if now == end:
        ans = dist
        break

    for v, t, h in graph[now]:
        newh = height - h
        if newh <= 0:
            continue

        cost = dist + t
        if distance[v][newh] > cost:
            distance[v][newh] = cost
            heapq.heappush(q, (cost, v, newh))

print(ans if ans is not None else -1)