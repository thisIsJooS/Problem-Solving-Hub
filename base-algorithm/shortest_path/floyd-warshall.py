INF = int(1e9)

# 노드의 개수 및 간선의 개수를 입력받기
n, m = map(int, input().split())

graph = [[INF]*(n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for i, j in zip(range(1, n+1), range(1, n+1)):
    graph[i][j] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    # A에서 B로 가는 비용은 C라고 설정
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

# 수행된 결과를 출력
for a in range(1, n+1):
    for b in range(1, n+1):
        # 도달할 수 없는 경우, 무한이라고 출력
        if graph[a][b] == INF:
            print('INF', end=" ")
        else:
            print(graph[a][b], end=" ")
    print()


'''input
4 7 
1 2 4
1 4 6 
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2

>>  0 4 8 6 
    3 0 7 9 
    5 9 0 4 
    7 11 2 0 
    
    
6 11
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

>>  0 2 3 1 2 4 
    INF 0 3 2 3 5 
    INF 3 0 5 6 5 
    INF 5 2 0 1 3 
    INF 4 1 6 0 2 
    INF INF INF INF INF 0 
'''