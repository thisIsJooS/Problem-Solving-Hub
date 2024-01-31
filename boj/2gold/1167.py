from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n):
    arr = deque(map(int, input().split()))

    v = arr.popleft()
    while len(arr) > 1:
        u, e = arr.popleft(), arr.popleft()
        graph[v].append((u, e))

ans = 0

def f(now, dist):
    global ans, next
    for v, c in graph[now]:
        if v not in visited:
            break
    else:
        return dist


    for v, c in graph[now]:
        if v not in visited:
            visited.add(v)
            val = f(v, dist+c)

            if ans < val:
                ans = val
                next = v


    return ans


start = 1
visited = set()
visited.add(start)
next = None
f(start, 0)
visited = set()
visited.add(next)
f(next, 0)

print(ans)


"""
6
1 2 3 -1
2 1 3 5 3 3 5 -1
3 2 5 4 7 -1
4 3 7 -1
5 2 3 6 5 -1
6 5 5 -1
"""
