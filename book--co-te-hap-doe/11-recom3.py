# https://school.programmers.co.kr/learn/courses/30/lessons/49191

def solution(n, results):
    answer = 0
    graph = [[1e9] * (n + 1) for _ in range(n + 1)]

    for r in results:
        a, b = r
        graph[a][b] = 1

    for i in range(n + 1):
        graph[i][i] = 0

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j: continue

            if graph[i][j] == 1e9 and graph[j][i] == 1e9:
                break
        else:
            answer += 1

    return answer