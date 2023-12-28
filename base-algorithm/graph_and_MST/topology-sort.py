from collections import deque

# 노드의 개수와 간선의 개수를 입력받기
v, e = map(int, input().split())

# 모든 노드에 대한 집입차수는 0으로 초기화
indegree = [0] * (v+1)

# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
graph = [[] for i in range(v+1)]

# 방향 그래프의 모든 간선 정보를 입력받기
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)      # 방향 그래프라서 a에만 b를 추가해준다.
    indegree[b] += 1    # 진입차수를 1 증가


def topology_sort():    # 위상정렬 함수
    result = []     # 알고리즘 수행 결과를 담을 리스트
    q = deque()     # 큐 기능을 위한 deque 라이브러리 사용

    # 처음 시작할 떄는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)


    while q:     # 큐가 빌 때까지 반복
        now = q.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:    # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
                q.append(i)

    print(result)


topology_sort()


"""input
7 8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4
>> [1, 2, 5, 3, 6, 4, 7]
"""
