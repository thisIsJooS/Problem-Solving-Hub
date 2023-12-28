# 다익스트라 알고리즘 이용
"""
양방향 가능, 1만큼의 시간
1 -> K -> X
"""
import heapq
INF = int(1e9)
n, m = map(int, input().split())        # 회사의 개수 , 경로의 개수

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

x, k = map(int, input().split())


def dijkstra(start, end):
    global n
    distance = [INF] * (n+1)
    distance[start] = 0

    q = []
    heapq.heappush(q, (0, start))   # (거리, 노드)

    while q:
        dist, node = heapq.heappop(q)

        if dist > distance[node]:
            continue

        for v in graph[node]:
            if distance[v] > dist + 1:
                distance[v] = dist+1
                heapq.heappush(q, (dist+1, v))

    return distance[end]


a = dijkstra(1, k)
b = dijkstra(k, x)
if a == INF or b == INF:
    print(-1)
else:
    print(a+b)


"""
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5
>> 3

4 2
1 3
2 4
3 4
>> -1
"""