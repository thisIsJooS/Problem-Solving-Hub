# https://school.programmers.co.kr/learn/courses/30/lessons/49189

import heapq
from collections import defaultdict


def solution(n, edge):
    answer = 0
    graph = defaultdict(list)

    for e in edge:
        a, b = e
        graph[a].append(b)
        graph[b].append(a)

    distance = [1e9] * (n + 1)

    q = []
    start = 1
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for v in graph[now]:
            cost = dist + 1
            if distance[v] > cost:
                distance[v] = cost
                heapq.heappush(q, (cost, v))

    distance = distance[1:]

    return len([d for d in distance if d == max(distance)])