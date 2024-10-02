from collections import defaultdict, deque

n = int(input())
arr = list(map(int, input().split()))
target = int(input())

graph = defaultdict(list)

for child, parent in enumerate(arr):
    if child == target:
        continue
    graph[parent].append(child)

graph[target] = list()

q = deque()
q.append(arr.index(-1))

ans = 0

while q:
    parent = q.popleft()

    if not graph[parent]:
        ans += 1

    for child in graph[parent]:
        q.append(child)

print(ans if target != arr.index(-1) else 0)