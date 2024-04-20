# https://school.programmers.co.kr/learn/courses/30/lessons/12978

import heapq
from collections import defaultdict


def solution(N, road, K):
    answer = 0

    INF = int(1e9)
    distance = defaultdict(lambda: INF)
    graph = defaultdict(list)

    for r in road:
        a, b, c = r
        graph[a].append((b, c))
        graph[b].append((a, c))

    start = 1
    distance[start] = 0

    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)

        if dist > distance[now]:
            continue

        for b, c in graph[now]:
            cost = dist + c
            if distance[b] > cost:
                distance[b] = cost
                heapq.heappush(q, (cost, b))

    return len([v for k, v in distance.items() if v <= K])