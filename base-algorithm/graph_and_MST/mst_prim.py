import heapq

v, e = map(int, input().split())
graph = [[] for i in range(v+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))     # (노드, 거리)
    graph[b].append((a, c))     # 무방향 그래프임을 가정하였으므로 양쪽 다 추가

start = 1       # 시작 정점을 1로 선택
visited = set()     # 방문한 정점을 저장하는 집합
q = [(0, start)]    # 간선을 저장할 최소 힙 리스트

mst = []    # 최소 신장 트리를 저장하는 리스트
res = 0     # 최종 비용을 담는 변수
while q:
    dist, now = heapq.heappop(q)

    if now in visited:      # 이미 방문한 경우 스킵
        continue
    visited.add(now)        # 방문 처리

    mst.append((now, dist)) # 최소 신장 트리에 현재 간선 추가
    res += dist

    # 현재 정점과 연결된 간선을 최소 힙에 추가
    for n, d in graph[now]:
        if n not in visited:
            heapq.heappush(q, (d, n))


print(mst)
print(res)


"""input
7 9
1 2 29
1 5 75
2 3 35
2 6 34
3 4 7
4 6 23
4 7 13
5 6 53
6 7 25

>> [(1, 0), (2, 29), (6, 34), (4, 23), (3, 7), (7, 13), (5, 53)]
>> 159
"""