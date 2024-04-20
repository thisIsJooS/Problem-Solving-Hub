# https://school.programmers.co.kr/learn/courses/30/lessons/72413


def solution(n, s, a, b, fares):
    answer, INF = int(1e9), int(1e9)

    graph = make_graph(n, fares)

    for k in range(1, n+ 1):
        answer = min(answer, graph[s][k] + graph[k][a] + graph[k][b])

    return answer


def make_graph(n, fares):
    INF = int(1e9)
    graph = [[INF] * (n + 1) for _ in range(n + 1)]

    for f in fares:
        a, b, c = f
        graph[a][b] = c
        graph[b][a] = c

    for i in range(n + 1):
        graph[i][i] = 0

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    return graph