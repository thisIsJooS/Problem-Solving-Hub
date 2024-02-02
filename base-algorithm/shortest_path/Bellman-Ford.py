"""
- 특정 출발 노드에서 다른 모든 노드까지의 최단 경로 탐색
- 음수 가중치 에지가 있어도 수행할 수 있음
- 전체 그래프에서 음수 사이클의 존재 여부를 판단할 수 있음
- 시간복잡도 O(VE)

벨만포드 vs 다익스트라
✅ 다익스트라 :
- 매번 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택한다.
- 음수 간선이 없다면 최적의 해를 찾을 수 있다
✅ 벨만 포드 :
- 매번 모든 간선을 전부 확인한다. 따라서 다익스트라 알고리즘에서의 최적의 해를 항상 포함한다.
- 다익스트라 알고리즘에 비해서 시간이 오래 걸리지만 음수 간선 순환을 탐지할 수 있다.
"""

INF = int(1e9)

n, m = map(int, input().split())    # 노드의 개수, 간선의 개수
edges = []                          # 모든 간선에 대한 정보를 담는 리스트 만들기
distance = [INF] * (n+1)            # 최단 거리 테이블을 모두 무한으로 초기화

# 모든 간선 정보를 입력하기
for _ in range(m):
    a, b, c = map(int, input().split())     # a에서 b로 가는 비용이 c
    edges.append((a, b, c))


def bf(start):
    distance[start] = 0     # 시작 노드에 대해서 초기화

    for i in range(n):      # 전체 n 번의 라운드를 반복
        for j in range(m):  # 매 반복마다 "모든 간선"을 확인하며
            now, next, cost = edges[j]
            if distance[now] != INF and distance[next] > distance[now] + cost:
                distance[next] = distance[now] + cost

                if i == n-1:        # n번째 라운드에서도 값이 갱신된다면 음수 순환이 존재
                    return True

    return False


# Bellman-Ford 알고리즘 수행
cycle = bf(1)       # 1번 노드에서 시작

if cycle:
    print("-1")
else:
    for i in range(2, n+1):
        if distance[i] == INF:
            print('-1')
        else:
            print(distance[i])

"""
3 4
1 2 4
1 3 3
2 3 -1
3 1 -2

>> 4 3

3 4
1 2 4
1 3 3
2 3 -4
3 1 -2

>> -1

3 2
1 2 4
1 2 3

>> 3 -1
"""
# https://www.acmicpc.net/problem/11657