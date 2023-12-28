import heapq
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for n, d in graph[now]:
            cost = dist + d
            if cost < distance[n]:
                distance[n] = cost
                heapq.heappush(q, (cost, n))

dijkstra(start)

for i in range(1, n+1):
    # 도달할 수 없는 경우, 무한(INF)라고 출력
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i], end=' ')