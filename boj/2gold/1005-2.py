from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

def f():
    n, k = map(int, input().split())
    weight = [0] + list(map(int, input().split()))
    graph = [[] for _ in range(n+1)]
    indeg = [0] * (n+1)
    for _ in range(k):
        a, b = map(int, input().split())
        graph[a].append(b)
        indeg[b] += 1

    q = deque()
    res = [0] * (n+1)
    for i in range(1, n+1):
        if indeg[i] == 0:
            res[i] = weight[i]
            q.append((i, res[i]))

    while q:
        now, w = q.popleft()

        for v in graph[now]:
            indeg[v] -= 1
            res[v] = max(res[v], weight[v] + w)

            if indeg[v] == 0:
                q.append((v, res[v]))

    end = int(input())
    return res[end]


for _ in range(t):
    print(f())