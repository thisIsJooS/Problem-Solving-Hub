# https://school.programmers.co.kr/learn/courses/30/lessons/43164

from collections import defaultdict


def solution(tickets):
    answer = []

    graph = defaultdict(list)
    for i, t in enumerate(tickets):
        a, b = t

        graph[a].append((b, i))

    for k in graph:
        graph[k].sort()

    start = 'ICN'

    def dfs(now, result, visited):
        nonlocal graph, answer

        if answer:
            return

        if len(result) - 1 == len(tickets):
            answer = result[:]
            return

        for v, i in graph[now]:
            if (now, v, i) in visited:
                continue

            dfs(v, result + [v], visited | {(now, v, i)})

    dfs(start, [start], set())

    return answer