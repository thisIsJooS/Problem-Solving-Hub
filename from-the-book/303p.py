import sys
from collections import deque
input = sys.stdin.readline
import copy

n = int(input())
time = [0]
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
q = deque()

for i in range(1, n+1):
    temp = list(map(int, input().split()))
    time.append(temp[0])    # 시간 추가

    if len(temp) > 2:   # 선수과목 존재
        for t in temp[1:-1]:
            graph[t].append(i)
            indegree[i] += 1

for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)

_time = copy.deepcopy(time)

while q:
    now = q.popleft()

    for v in graph[now]:
        _time[v] += time[now]
        indegree[v] -= 1

        if indegree[v] == 0:
            q.append(v)


print(*_time[1:])

"""
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1
"""