from heapq import heappush, heappop

n = int(input())
arr = []
for _ in range(n):
    a, b, c = map(int, input().split())
    arr.append((b, c))

arr.sort()

q = []
heappush(q, arr[0][1])

for i in range(1, n):
    if arr[i][0] >= q[0]:
        heappop(q)

    heappush(q, arr[i][1])

print(len(q))