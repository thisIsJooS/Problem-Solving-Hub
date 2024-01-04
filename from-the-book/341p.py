import sys
from collections import deque
from itertools import combinations
def count_safe(b):
    return sum(row.count(0) for row in b)

input = sys.stdin.readline
N, M = map(int, input().split())
graph = []
empty = []
virus = deque()
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(N):
    data = list(map(int, input().split()))
    graph.append(data)

    for j in range(M):
        if graph[i][j] == 0:
            empty.append((i, j))
        elif graph[i][j] == 2:
            virus.append((i, j))

import copy
res = 0
for comb in combinations(empty, 3):
    copied = copy.deepcopy(graph)
    q = copy.copy(virus)
    for x, y in comb:
        copied[x][y] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if not (0<=nx<N and 0<=ny<M): continue
            if copied[nx][ny] == 1: continue
            elif copied[nx][ny] == 0:
                copied[nx][ny] = 2
                q.append((nx, ny))


    count = count_safe(copied)
    res = max(res, count)

print(res)



