from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])      # 큐 구현을 위해 deque 라이브러리 사용

    visited[start] = True       # 현재 노드를 방문 처리

    while queue:                # 큐가 빌 때 까지 반복
        v = queue.popleft()     # 큐에서 원소를 하나 뽑아 출력
        print(v, end=' ')

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


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

visited = [False] * 9

bfs(graph, 1, visited)

# Result : 1 2 3 8 7 4 5 6