import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수를 입력받기
n, m = map(int, input().split())
# 시작 노드 번호를 입력 받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n+1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)
parent = [0 for i in range(n+1)]

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:    # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for v, c in graph[now]:
            cost = dist + c
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[v]:
                distance[v] = cost
                parent[v] = now
                heapq.heappush(q, (cost, v))


dijkstra(start)

for i in range(1, n+1):
    # 도달할 수 없는 경우, 무한(INF)라고 출력
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i], end=' ')

path = []
cur = n
while cur:
    path.append(cur)
    cur = parent[cur]
print('\n', path[::-1])

"""입력 예시
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2

>> 0 2 3 1 2 4 

4 7 
1
1 2 4
1 4 6 
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2
>> 0 4 8 6
"""