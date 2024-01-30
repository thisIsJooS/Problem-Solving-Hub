from collections import deque

n = int(input())
arr = []

for _ in range(n):
    arr.append(int(input()))

arr.sort()
arr = deque(arr)

ans = 0
while arr:

    ans = max(ans, len(arr) * min(arr))
    arr.popleft()

print(ans)