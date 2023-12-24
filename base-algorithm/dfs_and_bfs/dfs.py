def dfs(graph, v, visited):
    visited[v] = True   # 현재 노드를 방문 처리
    print(v, end= ' ')

    for i in graph[v]:  # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
        if not visited[i]:
            dfs(graph, i, visited)

def dfs_simple(v):
    visited[v] = True   # 현재 노드를 방문 처리
    print(v, end= ' ')

    for i in graph[v]:  # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
        if not visited[i]:
            dfs(graph, i, visited)


graph = [
    [],
    [2, 3, 8],  # 1번 노드는 2, 3, 8번 노드와 연결되어 있다
    [1, 7],     # 2번 노드는 1, 7번 노드와 연결되어 있다.
    [1, 4, 5],  # 이하동문
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현
visited = [False] * 9

dfs_simple(1)
# dfs(graph, 1, visited)

# Result : 1 2 7 6 8 3 4 5