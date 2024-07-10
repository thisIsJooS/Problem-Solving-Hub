from heapq import heappush, heappop

n = int(input())

schedules = []
for _ in range(n):
    a, b = map(int, input().split())
    schedules.append((a, b))

schedules.sort()

q = []
heappush(q, schedules[0][1])

for i in range(1, n):
    if schedules[i][0] >= q[0]:
        heappop(q)

    heappush(q, schedules[i][1])

print(len(q))